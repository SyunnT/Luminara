# Luminara

通过 Luminara，你可以便捷地在一个统一的页面中简单地管理自己的服务器系统以及你希望被管理的服务。



## 代码贡献指南

本项目使用`poetry`工具对依赖进行管理，安装方法如下：

你可以直接使用`pip`工具下载`poetry`，但建议使用`pipx`下载`poetry`，使用`pipx`安装的工具都运行在一个独立的虚拟环境中，可以使你的`poetry`和相关依赖与系统`python`环境分离。

- 安装`pipx`

  ```bash
  python -m pip install pipx
  ```

- 使用`pipx`安装`poetry`

  ```bash
  pipx install poetry
  ```

  使用该方法安装的`poetry`你可以在两个地方找到，一个是`pipx`为`poetry`建立的虚拟环境中，路径通常为`~/pipx/venvs/poetry/Scripts/`。另一个一般在`~/.local/bin/`中，该目录可以用来添加到系统环境变量。

- 使用`poetry`创建虚拟环境

  当你`clone`了本项目之后，建议为本项目创建一个虚拟环境，防止项目的依赖和其他环境相互交叉。

  首先，建议先更改`poetry`的一个默认配置项：

  ```bash
  poetry config virtualenvs.in-project true
  ```

  使用`poetry`创建的虚拟环境默认保存在一个统一的系统位置而非项目目录下，该命令可以修改其行为，使`poetry`创建的虚拟环境建立在项目目录下。

  接着，就可以使用`poetry`在项目中创建虚拟环境了：

  ```bash
  poetry env use python
  ```

  通常，该命令在执行命令的工作目录创建一个`.venv`文件夹，其中是虚拟环境的相关内容。

- 使用`poetry`管理依赖

  项目本身已经有了一些依赖项，我们统一使用`poetry`进行管理，所有相关信息保存在项目根目录中的`pyproject.toml`和`poetry.lock`两个文件中。

  你可以使用如下命令来安装已有的依赖项：

  ```bash
  poetry install
  ```

  如果要添加依赖，你可以简单的使用以下命令：

  ```bash
  poetry add <package_name>
  ```

  它会将新增的依赖项添加到上述的两个文件中，并在虚拟环境中安装对应的依赖项

  如果要移除依赖，使用如下命令：

  ```bash
  poetry remove <package_name>
  ```

- 使用虚拟环境运行代码

  如果按照前述的流程完成了虚拟环境的创建以及依赖的安装，那么所有的依赖将安装在项目的虚拟环境目录下，所以也需要使用该虚拟环境中的`python`解释器来运行代码，你可以直接通过目录访问到`.venv/Scripts/`目录下的`python`解释器，也可以先使用该目录下的虚拟环境激活脚本，然后就可以按照使用系统`python`环境一样使用虚拟环境中的`python`了。

  当你使用`cmd`或`powershell`时，请直接运行`activate.bat`脚本：

  ```powershell
  .venv/Scripts/activate.bat
  ```

  如果使用其他终端如`bash`时，请执行：

  ```bash
  source .venv/Scripts/activate
  ```

  正常情况下，此时你的终端就已经处于虚拟环境中了，需要注意的是虚拟环境只在当前终端生效，你可以根据终端用户输入提示前类似`(.venv) $ `的括号提示来判断当前是否处于虚拟环境中。

  如果要退出该环境，简单的执行：

  ```bash
  deactivate
  ```

  即可



## 使用指南
