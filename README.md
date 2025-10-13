# DjangoStack

A boilerplate base for projects with Django, Tailwindcss, Webpack, Postgress and pgvector technologies.

### Prerequisites for using Docker

Install Docker Desktop
  - Download from [Docker's official website](https://www.docker.com/products/docker-desktop/)
  - Follow installation instructions for your OS
  - Start Docker Desktop and wait until it's running

## 1. Set up Virtual Enviroment

Create and activate a virtual environment to manage dependencies:

```Bash
python -m venv .venv
.venv\Scripts\activate
```
---
## 2. Install Dependencies:

Install the required Python packages from requirements.txt:

```Bash
pip install -r requirements.txt
```
---
## 3. Install Node.js Dependencies:

You'll need to install Node.js dependencies:
```Bash
npm install
```
---
## 4. Create .env file
Copy env.dist to .env and fill in the necessary settings (e.g. database credentials)
---
## 5. Start PostgreSQL

```bash
docker-compose up -d
```
---

## 6. Run Migrations:

Apply any database migrations:
```Bash
cd core
python manage.py migrate
```
---
## 7. Run Webpack:

Depending on your Webpack configuration, you might need to run Webpack to build your frontend assets:
```Bash
npm run dev  # or `npm run prod` for production
```
---
## 8. Start the Django Development Server:

Finally, you can start the Django development server:
```Bash
python manage.py runserver
```

### License

My project is open‐source software released under the MIT License.
See the [LICENSE](./LICENSE) file for full license text.