// Crear dos listas, la primera debe ser generada de forma aleatoria y tener 5 elem
// La segunda debe ser ingresada por teclado (debe tener 5 enteros)
// Concatenar ambas listas
// Insertar en la 7°,8° y 9° posición los elementos 14,20 y 7
// Obtener el promedio de esa lista
// Por último ordenarlo de forma descendente la lista
import 'dart:io';
import 'dart:math';
void main() {
Random random = Random();
List lista_1 = List.generate(5, (index) => random.nextInt(10));
List <int> lista_2 = [];

print("Ingrese 5 números enteros: ");
for (int i = 0; i < 5; i++){
  stdout.write('Elemento ${i + 1}: ');
      int elemento = int.parse(stdin.readLineSync()!);
      lista_2.add(elemento);
}
List lista_3 = lista_1 + lista_2;
print("La lista generada de forma aleatoria es: $lista_1");
print("La lista concatenada entre la lista 1 y la lista 2 es: $lista_3");
lista_3.insertAll(5, [14,20,7]);
print("La lista con los elementos insertados queda: $lista_3");
lista_3.sort((a,b) => b.compareTo(a));
print("La lista ordenada descendentemente es: $lista_3");


}
