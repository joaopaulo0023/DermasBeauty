# Dermas Beauty

Site institucional para a clínica de estética e bem-estar Dermas Beauty.

## Requisitos

- Python 3.10+
- Django 5.0.7

## Como criar o ambiente virtual

```bash
python -m venv venv
```

### Windows

```powershell
venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar migrations

```bash
python manage.py migrate
```

## Criar superusuário

```bash
python manage.py createsuperuser
```

## Iniciar servidor

```bash
python manage.py runserver
```

## Acessos

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Observações

- O projeto usa SQLite e Django ORM.
- As configurações podem ser ajustadas em `.env`.
- Imagens e arquivos de mídia ficam em `media/` durante o desenvolvimento.
"# DermasBeauty" 
