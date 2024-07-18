# Hands-on Workshop on CNA Detection in Single-Cell RNA-Sequencing Data

- Instructors: Prof. Yuanhua HUANG, Rongting HUANG and Xianjie HUANG

- Date & Time: 2:00 pm - 5:30 pm, Friday, July 19, 2024

- Venue: Knowledge Hub, Yu Chun Keung Medical Library


## File architecture in all training accounts

![File architecture](./workshop_structure.png)


## Preprocessing

- xcltk: https://github.com/hxj5/xcltk

The submission of each pbs script would be simply: `qsub <pbs_script>`
e.g., `qsub pbs_baf`

## XClone

- github: https://github.com/single-cell-genetics/XClone

- tutorial: https://xclone-cnv.readthedocs.io/en/latest/



### demo

These demo can be used in [Google Colab](https://colab.google/) directly.

```python
pip install xclone
```


- [GX109_demo_notebooks](https://github.com/Rongtingting/xclone-data/tree/main/demo/GX109_demo_notebooks)

- [BCH869 demo](https://github.com/Rongtingting/xclone-data/blob/main/examples/BCH869_XClone_tutorials.ipynb)



### shell script

The submission of the pbs script would be simply: `qsub pbs_xclone`
