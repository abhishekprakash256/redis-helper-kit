### **📌 Development Documentation**

## **1. Requirements**
To set up and run this project, ensure you meet the following requirements:

- **Redis Installation**  
  - Install Redis **bare-metal** or run it using Docker:  
    ```bash
    # Run redis in Docker (recommended)

    docker pull redis

    docker run -d --name redis --network my_network -p 6379:6379 redis:latest  
    ```
  - Ensure the Redis server is running before testing or development.

- **Redis Connection Setup**
  - Configure the **redis client** in `Helper_Fun` class:
    - Use `"localhost"` if running MongoDB **locally**.
    - Use `"redis"` if running **inside Docker**.

- **Install Required Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

---

## **2. Project Structure**
```
├── DEVDOC.md
├── README.md
├── docs
│   └── DESIGN.md
├── examples
│   └── basic_usage.py
├── exp.py
├── pyproject.toml
├── redis_helper_kit
│   ├── __init__.py
│   ├── connection.py
│   └── redis_crud_operations.py
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── test_connection.py
    └── test_redis_crud_operations.py

```



## **3. Development & Branching Strategy**
This project follows a **structured Git workflow** with three main branch categories:  

### **🔹 `main` (Production)**
- The most **stable** branch containing **production-ready** code.  
- Only **tested and reviewed** changes are merged here.  
- **Deployment to production happens from `main`**.

### **🔹 `test` (Staging/Testing)**
- Used for **integration testing** before merging into `main`.  
- Acts as a **buffer** between `feature` branches and `main`.  
- **Continuous Integration (CI)** runs automated tests on this branch.  

### **🔹 `feature/*` (Feature Development)**
- Used for **new features, bug fixes, or improvements**.  
- **Naming Convention:**  
  - `feature/<feature-name>` (e.g., `feature/authentication`, `feature/api-refactor`)  
  - `bugfix/<bug-name>` (e.g., `bugfix/payment-error`)  
- Merged into `test` after development is complete.  

---

## **4. Git Workflow: Step-by-Step Guide**
### **🔹 Step 1: Creating a New Feature Branch**
Every new feature or bug fix starts from the latest `test` branch.

```bash
git checkout test
git pull origin test  # Ensure latest updates
git checkout -b feature/new-feature  # Create a new branch
```

Work on your feature, commit changes, and push to remote:

```bash
git add .
git commit -m "Added new feature: X"
git push origin feature/new-feature
```

---

### **🔹 Step 2: Merging Feature Branch into `test`**
Once development is complete, **create a Pull Request (PR)** from `feature/new-feature` → `test`.

- ✅ Ensure **all tests pass** before merging.
- ✅ Conduct **code reviews** for quality control.

If everything is fine, **merge into `test`**:

```bash
git checkout test
git pull origin test
git merge feature/new-feature
git push origin test
```

After merging, delete the feature branch:

```bash
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

---

### **🔹 Step 3: Merging `test` into `main`**
After multiple features are tested in `test`, merge into `main` for release.

```bash
git checkout main
git pull origin main
git merge test
git push origin main
```

🚀 **Deploy the `main` branch to production after merging!**

---

## **5. Best Practices for Git Workflow**
✅ **Keep `main` clean** → Never push directly to `main`; always merge from `test`.  
✅ **Frequent sync** → Regularly update `feature` branches from `test` to prevent merge conflicts.  
✅ **Use descriptive branch names** → Example: `feature/user-auth`, `bugfix/payment-error`.  
✅ **Delete merged branches** → Keep the repository clean by removing feature branches after merging.  
✅ **Code reviews & CI/CD** → Run automated tests on `test` before merging into `main`.  

---

## **6. Example Git Workflow**
```bash
# Create and work on a feature branch
git checkout test
git pull origin test
git checkout -b feature/new-api

# Work on code...
git add .
git commit -m "Implemented new API feature"
git push origin feature/new-api

# Merge into test after review
git checkout test
git pull origin test
git merge feature/new-api
git push origin test

# Merge tested code into main
git checkout main
git pull origin main
git merge test
git push origin main
```

---

## **7. Running Tests with Pytest**
To run **unit tests** locally:
```bash
pytest --maxfail=5 --disable-warnings -v
```
- **`--maxfail=5`** → Stops execution after **5 failures**.  
- **`--disable-warnings`** → Suppresses warnings for cleaner output.  
- **`-v`** → Enables **verbose output** for better debugging.  

---

## **8. Automated Testing with GitHub Actions**
The project uses **GitHub Actions** to run tests on every push or pull request.

### **📌 GitHub Actions Workflow (`.github/workflows/ci.yml`)**
```yaml
name: Run Pytest

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
      - test
      - "feature/**"

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'  # Change to match your project

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run pytest
        run: pytest --maxfail=2 --disable-warnings -v
```

🚀 **Now, every commit gets tested automatically!**    

---

## **9. Deployment Strategy**
- **Staging (`test`)**: Run CI/CD tests before merging to `main`.  
- **Production (`main`)**: After merging from `test`, deploy the latest stable code.  

---

### **📌 Summary**
✅ **Structured Git workflow** with `main`, `test`, and `feature` branches.  
✅ **Automated testing** with `pytest` and GitHub Actions.  
✅ **Best practices** for feature development, merging, and deployment.  
✅ **Easy setup** with MongoDB (bare-metal or Docker).  
