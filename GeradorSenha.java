import java.security.SecureRandom;

public class GeradorSenha {
    public static void main(String[] args) {
        int tamanho = Integer.parseInt(args[0]);
        boolean usarLetras = Boolean.parseBoolean(args[1]);
        boolean usarNumeros = Boolean.parseBoolean(args[2]);
        boolean usarSimbolos = Boolean.parseBoolean(args[3]);

        String letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String numeros = "0123456789";
        String simbolos = "!@#$%&*()-_=+<>?/";

        String chars = "";
        if (usarLetras) chars += letras;
        if (usarNumeros) chars += numeros;
        if (usarSimbolos) chars += simbolos;

        if (chars.isEmpty()) {
            System.out.println("Escolha ao menos um tipo de caractere.");
            return;
        }

        SecureRandom random = new SecureRandom();
        StringBuilder senha = new StringBuilder();

        for (int i = 0; i < tamanho; i++) {
            int index = random.nextInt(chars.length());
            senha.append(chars.charAt(index));
        }

        System.out.println(senha.toString());
    }
}
