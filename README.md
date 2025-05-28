Health Check
Método: GET /health
Descripción: Verifica que el servicio está activo.
Respuesta:

Código: 200 OK

Body: { "status": "ok" }

Listar Usuarios
Método: GET /users
Descripción: Obtiene la lista de todos los usuarios.
Respuesta:

Código: 200 OK

Body: { "users": [ { "id": 1, "name": "Carlos Pérez", "email": "carlos.perez@example.com" }, { "id": 2, "name": "María Gómez", "email": "maria.gomez@example.com" } ] }

Crear Usuario
Método: POST /users
Descripción: Crea un nuevo usuario.
Body (JSON):
{ "name": "Nombre Apellido", "email": "correo@example.com" }
Respuesta:

Código: 201 Created

Body: { "user": { "id": 3, "name": "Nombre Apellido", "email": "correo@example.com" } }

Actualizar Usuario
Método: PUT /users/{user_id}
Descripción: Actualiza los datos de un usuario existente.
Parámetros: user_id (ID del usuario a modificar)
Body (JSON):
{ "name": "Nuevo Nombre", "email": "nuevo@example.com" }
Respuesta:

Código: 200 OK

Body: { "user": { "id": user_id, "name": "Nuevo Nombre", "email": "nuevo@example.com" } }

Eliminar Usuario
Método: DELETE /users/{user_id}
Descripción: Elimina un usuario.
Parámetros: user_id (ID del usuario a eliminar)
Respuesta:

Código: 204 No Content

Body: (vacío)
