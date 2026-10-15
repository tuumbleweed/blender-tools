# Fist Pose Cleaner

A Blender add-on that replaces finger animation in the active action with a static closed-fist pose. Useful for cleaning up hands in motion-capture animations on Auto-Rig Pro rigs.

## Installation

The add-on declares Blender 5.0 as its minimum version.

1. Download `fist-pose-cleaner.py` from this directory.
2. In Blender, open **Edit → Preferences → Add-ons** and choose **Install from Disk** from the menu.
3. Select the downloaded Python file and enable **Fist Pose Cleaner**.

## Usage

1. Select the Auto-Rig Pro armature and make the animation you want to edit its active action.
2. In the 3D Viewport, open the sidebar with **N** and select the **Animation** tab.
3. In **Fist Pose Cleaner**, click **Apply Static Fists**.
4. Check the hand pose across the animation. Repeat for other actions as needed.

Save a copy of your animation before applying: the add-on removes existing animation curves for the targeted controls and does not declare undo support.

## How it works

The add-on clears animation for both hands’ finger and fist controls, resets their transforms, scales `c_fist.r` and `c_fist.l` to `(0.5, 0.5, 0.5)`, and inserts one replacement transform key per control. It then restores the scene’s original frame.

It expects three segments for each finger, named `c_thumb1`–`c_thumb3`, `c_index1`–`c_index3`, `c_middle1`–`c_middle3`, `c_ring1`–`c_ring3`, and `c_pinky1`–`c_pinky3`, with `.r` and `.l` suffixes.

## Limitations

- Processes one active action at a time.
- Uses fixed control names and fist scale; the resulting pose depends on the rig. Missing controls produce warnings and are skipped.
- Removes all animation curves for the targeted bone paths, including custom-property animation.
- Clears matching curves across all channel bags in the action; take care with shared actions containing multiple slots.
- No automated tests or example scenes are included.
