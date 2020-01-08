# Data Analytics and Visualization

## Resources

* <https://towardsdatascience.com/autoviz-a-new-tool-for-automated-visualization-ec9c1744a6ad>
* <https://podcasts.apple.com/us/podcast/codenewbie/id919219256?i=1000372644598>
* <https://www.greatlearning.in/blog/weekly-guide-data-science-and-analytics-december/>
* <https://www.vox.com/recode/2019/12/18/21026229/nyc-ai-algorithms-shadow-report>

## Matplotlib

* <https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/marker_reference.html>
* <https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline>
* <https://matplotlib.org/3.1.1/faq/troubleshooting_faq.html>
* <https://matplotlib.org/examples/index.html>
* <https://www.youtube.com/watch?v=f_J8QU1m0Ng>
* Color schemes are important.  There are some handy suggestions, including accessible color schemes, from <https://colorbrewer2.org>
* Built-in color schemes based on those from ColorBrewer are available in matplotlib (<https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html>)
* To use a color scheme, you need to specify in the plot command c=<list of data to color>, cmap='<color scheme>'
* Plotting labels on bars themselves (or elsewhere within a graph, rather than on the axis)
  * <https://www.science-emergence.com/Articles/How-to-add-text-on-a-bar-with-matplotlib-/>

```bash
import random
import matplotlib.pyplot as plt
import numpy as np
x_limit = 100
x_axis = np.arange(0, x_limit, 1)
data = [random.random() for value in x_axis]
color_data = [random.random() for value in x_axis]
plt.scatter(x_axis, data, marker="o", c=color_data, s=x_axis, alpha=0.75, cmap='Dark2')
plt.colorbar()
```

### Data Visualization

* <https://socviz.co/>

### Jupyter Notebook

* something cool you can do in your Jupyter notebook to enhance your visual display of information: 
  * <https://twitter.com/TedPetrou/status/1196113338217877505>
* Jupyter Notebook
  * <https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/>
* Convert notebook to .py file: <https://github.com/jupyter/nbconvert>

```bash
jupyter nbconvert --to python PyBank.ipynb
```

### Python

* Python String Formatting
  * <https://www.techbeamers.com/python-format-string-list-dict/>
  * <https://www.py4e.com/book.php>
  * <https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3>
  * <https://pygrail.com/?code=90fb07d3>
  * Python Activities
    * <https://www.youtube.com/watch?v=TjWOZDY00WA&feature=youtu.be>
    * <https://www.youtube.com/watch?v=Y3TRABzAfho&feature=youtu.be>
    * <https://www.youtube.com/watch?v=Logbtv4oQlc&feature=youtu.be>
* <https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/>
* Python and Machine Learning: <https://www.humblebundle.com/books/python-machine-learning-packt-books>

### Pandas

* Using loc and iloc in panda dataframes
  * <https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/>
  * <http://scrapingauthority.com/pandas-dataframe-filtering/>
* How to create a correlation matrix using pandas: <https://datatofish.com/correlation-matrix-pandas/>

  ```bash
  plt.matshow(dataframe.corr())
  plt.show()
  ```


### Git and GitHub

* <https://blog.red-badger.com/2016/11/29/gitgithub-in-plain-english>
* <https://mukulrathi.com/git-beginner-cheatsheet/>
* <https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account>
* <https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh>

###  VBA

* <https://www.udemy.com/course/excel-vba-and-macros-course/>
* <https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ef38e600-6abe-4041-8118-a94000f7a375>

### Terminal Basics

```bash
# Terminal Basics
​
## Navigation
* Print Working Directory: `pwd`
* List files in directory: `ls`
* List all files in directory (including hidden files): `ls -a`
* List all files with long format: `ls -al`
* Change Directory to home directory: `cd`
* Change to Directory: `cd <directory_name>`
* Change Directory up one level: `cd ..`
* Create a Directory: `mkdir <directory_name>`
​
## File operations
* Create an empty file: `touch <filename>`
* Remove a file (be careful!): `rm <filename>`
* Remove a directory and all its files/subdirectories (be *very* careful!): `rm -r <directory>`
* Copy a file: `cp <source> <destination>`
* Move (or rename) a file: `mv <source> <destination>`
​
## Other useful stuff
* To repeat a previously-used command, use the up arrow to go back through your command history.
* Most commands have a `--help` option that will give much more information about the usage of the command and its additional features, e.g.: `ls --help`
* The `TAB` key will help auto-complete names (e.g. filenames, directories) in the terminal
* To clear the terminal window, you can use the command: `clear`
* `CTRL-L` will also clear the terminal window
* To stop a running command, use `CTRL-C`
```