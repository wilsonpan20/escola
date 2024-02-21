from rest_framework import viewsets, generics
from escola.models import Aluno,Curso,Matricula
from escola.serializer import AlunoSerializer, CursoSerializer,MatriculaSerializer,ListaMatriculasAlunoSerializer,ListaAlunosMatriculadosEmUmCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
class MatriculaViewSet(viewsets.ModelViewSet):
   """Exibindo todas as matriculas"""
   queryset = Matricula.objects.all()
   serializer_class = MatriculaSerializer 
   authentication_classes = [BasicAuthentication]
   permission_classes = [IsAuthenticated]
   
   
   
   
class ListaMatriculasAlunoViewSet(generics.ListAPIView):
   """Listando as Matriculas de aluno ou aluna"""
   def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
      
   serializer_class = ListaMatriculasAlunoSerializer
   authentication_classes = [BasicAuthentication]
   permission_classes = [IsAuthenticated]

class ListaMatriculaAlunoEmUmCursoViewSet(generics.ListAPIView):
    """Listando as curso de aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
      
    serializer_class = ListaAlunosMatriculadosEmUmCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
         