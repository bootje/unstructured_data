# Development Environment Setup

This repository provides a pre-configured development environment using VS Code and DevContainers. It simplifies the setup process by installing all necessary Python packages inside a containerized environment.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com/)

## Getting Started

1. **Clone the Repository**
   ```sh
   git clone https://github.com/bootje/unstructured_data.git
   cd your-repo
   ```

2. **Open in VS Code**
   - Open VS Code
   - Select `File > Open Folder...` and choose the cloned repository folder

3. **Rebuild the DevContainer**
   - Open the Command Palette (`Ctrl + Shift + P` or `Cmd + Shift + P` on macOS)
   - Select `Dev Containers: Rebuild and Reopen in Container`
   - Wait for the build to complete (this may take a while on the first run)

## Notes on Container Builds

- **First build time**: The initial build process can take quite a while, as all required packages are installed.
- **Speeding up future builds**:
  - If you only need to install additional Python packages, use:
    ```sh
    uv pip install package_name
    ```
    Then, manually add the package to `requirements-dev.txt` to persist it.
  - If you do not modify `Dockerfile` or `requirements-core.txt`, future rebuilds will use cached layers and be significantly faster.

## Useful Links

- [VS Code Remote - Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Guide: Cloning a Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- [uv: A faster alternative to pip](https://github.com/astral-sh/uv)

---

Now you're all set up! 🚀 Happy coding!

