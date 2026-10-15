bl_info = {
    "name": "Fist Pose Cleaner",
    "author": "Vladislav",
    "version": (1, 0, 0),
    "blender": (5, 0, 0),
    "location": "3D View > Sidebar > Animation",
    "description": "Replace finger animation with static fist pose",
    "category": "Animation",
}

import bpy


SIDES = ["r", "l"]

FINGER_BASE_NAMES = [
    "c_thumb1",
    "c_thumb2",
    "c_thumb3",

    "c_index1",
    "c_index2",
    "c_index3",

    "c_middle1",
    "c_middle2",
    "c_middle3",

    "c_ring1",
    "c_ring2",
    "c_ring3",

    "c_pinky1",
    "c_pinky2",
    "c_pinky3",
]

FIST_SCALE = (0.5, 0.5, 0.5)


def reset_bone_transform(bone):
    bone.location = (0.0, 0.0, 0.0)
    bone.scale = (1.0, 1.0, 1.0)

    if bone.rotation_mode == "QUATERNION":
        bone.rotation_quaternion = (1.0, 0.0, 0.0, 0.0)

    elif bone.rotation_mode == "AXIS_ANGLE":
        bone.rotation_axis_angle = (0.0, 0.0, 1.0, 0.0)

    else:
        bone.rotation_euler = (0.0, 0.0, 0.0)


def key_bone_transform(bone, frame):
    bone.keyframe_insert(
        data_path="location",
        frame=frame,
        group=bone.name,
    )

    if bone.rotation_mode == "QUATERNION":
        bone.keyframe_insert(
            data_path="rotation_quaternion",
            frame=frame,
            group=bone.name,
        )

    elif bone.rotation_mode == "AXIS_ANGLE":
        bone.keyframe_insert(
            data_path="rotation_axis_angle",
            frame=frame,
            group=bone.name,
        )

    else:
        bone.keyframe_insert(
            data_path="rotation_euler",
            frame=frame,
            group=bone.name,
        )

    bone.keyframe_insert(
        data_path="scale",
        frame=frame,
        group=bone.name,
    )


class ANIM_OT_apply_static_fists(bpy.types.Operator):
    bl_idname = "anim.apply_static_fists"
    bl_label = "Apply Static Fists"
    bl_description = (
        "Delete finger animation from the current action "
        "and replace it with static closed fists"
    )

    @classmethod
    def poll(cls, context):
        obj = context.object

        return (
            obj is not None
            and obj.type == "ARMATURE"
            and obj.animation_data is not None
            and obj.animation_data.action is not None
        )

    def execute(self, context):
        obj = context.object
        action = obj.animation_data.action

        finger_bones = [
            f"{name}.{side}"
            for side in SIDES
            for name in FINGER_BASE_NAMES
        ]

        fist_controllers = [
            f"c_fist.{side}"
            for side in SIDES
        ]

        bones_to_clean = finger_bones + fist_controllers

        bone_prefixes = tuple(
            f'pose.bones["{bone_name}"]'
            for bone_name in bones_to_clean
        )

        removed = 0

        # Delete existing finger/fist animation.
        for layer in action.layers:
            for strip in layer.strips:

                if not hasattr(strip, "channelbags"):
                    continue

                for channelbag in strip.channelbags:
                    for fcurve in list(channelbag.fcurves):

                        if fcurve.data_path.startswith(bone_prefixes):
                            channelbag.fcurves.remove(fcurve)
                            removed += 1

        first_frame = int(action.frame_range[0])
        original_frame = context.scene.frame_current

        context.scene.frame_set(first_frame)

        # Reset fingers.
        for bone_name in finger_bones:
            bone = obj.pose.bones.get(bone_name)

            if bone is None:
                self.report(
                    {"WARNING"},
                    f"Bone not found: {bone_name}",
                )
                continue

            reset_bone_transform(bone)

        # Apply fist controllers.
        for fist_name in fist_controllers:
            fist = obj.pose.bones.get(fist_name)

            if fist is None:
                self.report(
                    {"WARNING"},
                    f"Fist controller not found: {fist_name}",
                )
                continue

            reset_bone_transform(fist)
            fist.scale = FIST_SCALE

        # Key one static pose at the first frame.
        for bone_name in bones_to_clean:
            bone = obj.pose.bones.get(bone_name)

            if bone is None:
                continue

            key_bone_transform(
                bone,
                first_frame,
            )

        context.view_layer.update()
        context.scene.frame_set(original_frame)

        self.report(
            {"INFO"},
            f"Static fists applied to {action.name}; "
            f"removed {removed} F-curves",
        )

        return {"FINISHED"}


class VIEW3D_PT_fist_pose_cleaner(bpy.types.Panel):
    bl_label = "Fist Pose Cleaner"
    bl_idname = "VIEW3D_PT_fist_pose_cleaner"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    # This becomes the N-panel tab name.
    bl_category = "Animation"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        if (
            obj is None
            or obj.type != "ARMATURE"
        ):
            layout.label(
                text="Select an armature.",
            )
            return

        if (
            obj.animation_data is None
            or obj.animation_data.action is None
        ):
            layout.label(
                text="No active action.",
            )
            return

        action = obj.animation_data.action

        layout.label(
            text=f"Action: {action.name}",
        )

        layout.operator(
            "anim.apply_static_fists",
            text="Apply Static Fists",
            icon="HAND",
        )


classes = (
    ANIM_OT_apply_static_fists,
    VIEW3D_PT_fist_pose_cleaner,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
