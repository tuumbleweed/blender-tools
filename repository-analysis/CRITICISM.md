# Review notes

## Remaining Issues

- **Action-wide deletion can affect other slots.** Confirmed: `execute` traverses every channel bag in every layer/strip (lines 134–145), then keys through the selected object. In a shared, multi-slot action, matching controls in other slots may lose animation. Filter deletion to the selected object’s action slot.
- **No declared undo support or rig preflight.** Confirmed: the operator lacks `bl_options = {'REGISTER', 'UNDO'}` and deletes curves before checking bone existence. An incompatible or partially matching rig can receive a partial rewrite while the operator reports completion. Validate required controls before mutation and provide undo support.
- **Replacement timing is measured after deletion.** Confirmed: `action.frame_range` is read at line 147 after curves are removed and is truncated to an integer. Deletion can change the computed range, and fractional start frames are lost. Capture the intended start before modification and preserve its precision.
- **Broad path matching removes custom-property animation too.** Confirmed: line 143 matches the bone path prefix without restricting transform properties. If only transform replacement is intended, filter location, rotation, and scale paths explicitly; otherwise document this behavior.
- **Rig behavior is unverified.** Potential concern: fixed names and uniform 0.5 fist scale rely on specific rig behavior. No sample scene or tests establish that the intended fist pose is produced. A small representative scene and manual compatibility check would provide useful evidence before broader reuse.

## Simplification Opportunities

Keep each future utility self-contained while the collection is small. For this add-on, centralizing the fixed rig names and fist scale in one documented preset would make adaptation easier without introducing a general plugin framework. The current constants already provide a useful starting point.
