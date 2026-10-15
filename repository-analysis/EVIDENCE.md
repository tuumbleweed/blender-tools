# Evidence and review notes

## Sources inspected

Inspected the complete tracked tree: `README.md` and all 266 lines of `fist-pose-cleaner.py`; Git status, remotes, refs, and full locally available history. `main`, `origin/main`, and `origin/HEAD` all resolve to `30bf20f89712c8a0916475912cf53ad375bb080c`. No tags, other branches, tests, configurations, assets, or prior analysis files were present. No remote fetch or add-on execution was performed. No external evidence was needed for the code-level conclusions.

## Claim ledger

| Claim | Evidence | Confidence |
| --- | --- | --- |
| The repository currently contains one Blender Python add-on. | Tracked tree; root `README.md`; `fist-pose-cleaner.py`, `bl_info`, operator, panel, registration functions; implementation commit `5a15eefd778a5991ed4c4c27bb548fe5870a083d`. | High: complete small tree inspected. |
| Each invocation targets the active action, not every mocap action. | `ANIM_OT_apply_static_fists.poll` and `execute`, lines 98–111. Same implementation commit. | High: explicit action lookup; no action iteration. |
| Both hands’ named finger/fist curves are deleted across action channel bags, then transforms are keyed once. | `SIDES`, `FINGER_BASE_NAMES`, `FIST_SCALE`; `execute`, lines 113–192. Same implementation commit. | High for implementation; successful visual outcome untested. |
| Rotation reset/keying supports three rotation representations; missing bones are skipped with warnings. | `reset_bone_transform`, `key_bone_transform`, `execute`, lines 41–87 and 153–189. Same implementation commit. | High: explicit branches. |
| The add-on declares Blender 5.0 minimum and provides an Animation sidebar panel. | `bl_info`, `VIEW3D_PT_fist_pose_cleaner`, `register`, main guard. Same implementation commit. | High for declaration; runtime compatibility unverified. |
| Auto-Rig Pro mocap use was reported by the owner. | User-provided context; control names in source are consistent with that account but do not independently prove rig compatibility or actual usage. | Medium for intended workflow; no scene, dependency, or usage record. |
| Implementation contributions are represented in Git, but exclusive authorship is not proven. | Initial implementation commit; one observed Git author; `bl_info` author field. | Medium: no attribution or provenance documentation beyond these records. |

## Timeline basis

Earliest observed activity: `5a15eefd778a5991ed4c4c27bb548fe5870a083d`, September 23, 2026 at 17:56:39 −05:00, adds the entire add-on. Latest: `30bf20f89712c8a0916475912cf53ad375bb080c`, the same day at 17:58:20 −05:00, adds the README. Author and committer timestamps agree. Only two commits are available; no longer development phases or continuous work can be established. Actual project start/end and current maintenance status remain unknown.

## Context reconciliation and uncertainties

- Confirmed: one plugin currently exists. The recollection of rewriting all mocap fists may describe repeated manual use; the implementation handles one active action per invocation.
- Auto-Rig Pro compatibility and satisfactory closed-fist results require a representative rig and animation to verify. No supported rig version is established.
- Future small plugins are the owner’s stated intention, not implemented features or an established delivery schedule.
- Personal versus professional use, exclusive ownership, code origin, and permission to publish remain unconfirmed. No evidence identifies this repository as a fork, tutorial, or imported package; standalone is the current structural classification.
- The remote identifies a repository URL but does not establish public visibility. No measured time savings, production deployment, or usage scale is evidenced.

## Publication risks

No obvious embedded credentials or confidential scene data were found in the two tracked files. No license is included, so redistribution terms and any third-party provenance should be confirmed before publication. Public contribution wording requires owner review; repository history alone cannot establish exclusive authorship. The analysis deliberately omits Git email addresses. Auto-Rig Pro usage is an attributed owner report, not an affiliation or verified compatibility claim.

## Owner correction after analysis

The owner clarified that the add-on is installed and enabled in Blender and used through its panel, rather than run from the Text Editor. Documentation now reflects this workflow. The working tree also relocates the unchanged implementation to `fist-pose-cleaner/fist-pose-cleaner.py`; source paths above refer to the analyzed Git commit. A separate `fist-pose-cleaner/README.md` documents the add-on, and the collection README links to it. Installation was not independently runtime-tested.
