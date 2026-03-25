# 🐍 Django Learning Journey

```
╔═══════════════════════════════════════════════════════════╗
║   from zero import django                                 ║
║   while not mastered:                                     ║
║       learn()                                             ║
║       build()                                             ║
║       break_things()                                      ║
║       fix_things()                                        ║
╚═══════════════════════════════════════════════════════════╝
```

> **"First, solve the problem. Then, write the code."**
> Building toward ML/AI backend engineering — one migration at a time.

---

## 🗺️ What's Inside

This repo is my hands-on Django learning log — every folder is a chapter,
every bug is a lesson, every working endpoint is a win.

```
django_learning/
│
├── 📁 ch1  →  Hello World. The basics. urls → views → response.
├── 📁 ch6  →  Function-Based Views. HttpResponse. MVT clicks.
├── 📁 ch7  →  Multiple apps. URL routing. include(). No more chaos.
├── 📁 ch10 →  Templates. DTL. render(). Separation of concerns.
├── 📁 ch14 →  Template inheritance. base.html. DRY HTML finally.
└── 📁 product_crud → Full CRUD API. JsonResponse. Zero DRF. Pure Django.
```

---

## 🧱 The Stack

| Layer | Tech |
|---|---|
| Backend Framework | Django 5 |
| Database | SQLite → PostgreSQL (later) |
| API Layer | JsonResponse → DRF (next) |
| Auth | JWT (coming soon) |
| ML Integration | scikit-learn + joblib (goal) |
| Frontend | Streamlit (for ML demos) |

---

## 📍 Current Progress

- [x] Django project structure & MVT architecture
- [x] Function-based views & URL routing
- [x] Multiple apps, `include()`, URL namespacing
- [x] Django Templates & DTL (filters, tags, inheritance)
- [x] ORM — models, migrations, querysets
- [x] Dynamic URLs & path converters
- [x] JsonResponse & REST API basics
- [x] Full CRUD API with Class-Based Views
- [ ] Django REST Framework (DRF) ← currently here
- [ ] JWT Authentication
- [ ] ML model → API endpoint
- [ ] Streamlit frontend calling Django API

---

## 🔥 The Goal

```python
# what I'm building toward:

@api_view(['POST'])
def predict(request):
    data       = request.data['features']
    model      = joblib.load('model.pkl')
    prediction = model.predict([data])

    return Response({
        'prediction':  int(prediction[0]),
        'confidence':  0.94,
        'status':      'success'
    })
```

A production-ready **ML Prediction API** with:
- DRF endpoints
- JWT-protected routes
- scikit-learn model serving
- Streamlit frontend calling the API

---

## 💡 Key Lessons Learned

```python
# lesson 1 — never name your function after a built-in
def list(req): ...      # ❌ breaks list() everywhere
def list_data(req): ... # ✅

# lesson 2 — always run BOTH migration commands
python manage.py makemigrations  # generates instructions
python manage.py migrate         # actually builds the table

# lesson 3 — QuerySet is not JSON serializable
return JsonResponse(Product.objects.all())           # ❌ crashes
return JsonResponse(list(Product.objects.values()))  # ✅

# lesson 4 — safe=False for lists
return JsonResponse(['a', 'b', 'c'])              # ❌ TypeError
return JsonResponse(['a', 'b', 'c'], safe=False)  # ✅
```

---

## 🚀 Running Any Project

```bash
# clone the repo
git clone https://github.com/yourusername/django_learning.git
cd django_learning/<chapter_folder>

# setup environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# install dependencies
pip install django

# run migrations & start server
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `localhost:8000` and you're in.

---

## 📚 Learning Resources

| Resource | Used For |
|---|---|
| Geeky Shows (YouTube) | Main Django course |
| Django Official Docs | Reference & deeper understanding |
| This repo | Actually building things |

---

## 🧠 About

CS student grinding toward **ML/AI Backend Engineering**.
Learning Django not just to make websites — but to build APIs that serve machine learning models.

The dream: a clean REST API where Streamlit sends patient data and Django returns a cancer prediction. Building toward it one `python manage.py runserver` at a time.

---

<div align="center">

**Made with 🐛 bugs, ☕ chai, and stubbornness**

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?style=flat-square&logo=django)
![Status](https://img.shields.io/badge/Status-Learning-orange?style=flat-square)
![Bugs](https://img.shields.io/badge/Bugs_Fixed-countless-red?style=flat-square)

</div>
