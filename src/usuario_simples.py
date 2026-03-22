import hashlib

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha_hash = self._hash_senha(senha)

    def _hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def verificar_senha(self, senha):
        return self.senha_hash == self._hash_senha(senha)


class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, email, senha):
        if self.buscar_usuario(email):
            raise ValueError("Email já cadastrado")
        
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)

    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def login(self, email, senha):
        usuario = self.buscar_usuario(email)
        if usuario and usuario.verificar_senha(senha):
            return True
        return False

    def listar_usuarios(self):
        return [(u.nome, u.email) for u in self.usuarios]
