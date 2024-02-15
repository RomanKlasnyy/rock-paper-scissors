import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class RockPaperScissors {
    private static List<String> options = new ArrayList<>();
    private static boolean defaultGame = false;
    private static String name;
    private static int score = 0;
    private static boolean newUser = true;
    private static List<String> newRating = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        name = scanner.nextLine();
        System.out.printf("Hello, %s%n", name);

        try {
            File file = new File("rating.txt");
            Scanner fileScanner = new Scanner(file);
            while (fileScanner.hasNextLine()) {
                String line = fileScanner.nextLine();
                String[] lineList = line.split(" ");
                if (name.equals(lineList[0])) {
                    newUser = false;
                    score = Integer.parseInt(lineList[1]);
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }

        if (scanner.hasNextLine()) {
            String gestures = scanner.nextLine();
            if (gestures.isEmpty()) {
                options = Arrays.asList("rock", "scissors", "paper");
                defaultGame = true;
            } else {
                options = Arrays.asList(gestures.split(","));
            }
        }

        System.out.println("Okay, let's start");

        if (defaultGame) {
            playGame(scanner);
        } else if (options.size() % 2 != 0) {
            playGame(scanner);
        } else {
            playGame(scanner);
        }
    }

    private static void playGame(Scanner scanner) {
        Random random = new Random();
        while (true) {
            String action = scanner.nextLine();
            String cAction = options.get(random.nextInt(options.size()));

            if (action.equals("!exit")) {
                System.out.println("Bye!");
                if (newUser) {
                    newUser();
                } else {
                    updateUser();
                }
                break;
            }

            if (action.equals("!rating")) {
                System.out.println("Your rating: " + score);
                continue;
            }

            if (action.equals("!help")) {
                helpOption();
                continue;
            }

            if (options.contains(action)) {
                int halfList = (options.size() - 1) / 2;
                int actionId = options.indexOf(action);
                int cActionId = options.indexOf(cAction);

                if (action.equals(cAction)) {
                    System.out.printf("There is a draw (%s) (+50 points)%n", action);
                    score += 50;
                } else if (actionId + halfList <= options.size()) {
                    if (cActionId > actionId && actionId >= cActionId - halfList) {
                        System.out.printf("Sorry, but computer chose %s%n", cAction);
                    } else {
                        System.out.printf("Well done. Computer chose %s and failed (+100 points)%n", cAction);
                        score += 100;
                    }
                } else {
                    if (cActionId < actionId && actionId <= cActionId + halfList) {
                        System.out.printf("Well done. Computer chose %s and failed (+100 points)%n", cAction);
                        score += 100;
                    } else {
                        System.out.printf("Sorry, but computer chose %s%n", cAction);
                    }
                }
            } else {
                System.out.println("Invalid input. Type \"!help\" for help");
            }
        }
    }

    private static void newUser() {
        try {
            FileWriter writer = new FileWriter("rating.txt", true);
            writer.write(name + " " + score + "\n");
            writer.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace(System.out);
        }
    }

    private static void updateUser() {
        try {
            File file = new File("rating.txt");
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String data = scanner.nextLine();
                String[] dataList = data.split(" ");
                if (name.equals(dataList[0])) {
                    newRating.add(name + " " + score);
                } else {
                    newRating.add(data);
                }
            }
            FileWriter writer = new FileWriter("rating.txt");
            for (String s : newRating) {
                writer.write(s + "\n");
            }
            writer.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace(System.out);
        }
    }

    private static void helpOption() {
        String gameType = defaultGame ? "classic version" : "your optional version";
        System.out.printf("Hi, %s. You are playing %s of the game%n", name, gameType);
        System.out.println("Your available options for the game are:");
        System.out.println(options);
        System.out.println();
        System.out.println("To play a game, type one of the options");
        System.out.println("The option beats the next half of options, but loses to the previous ones");
        System.out.println("If you win, you get +100 points. Draw: +50 points. Lose: +0 points");
        System.out.println();
        System.out.println("Type \"!exit\" to exit your game. Your score will be added/updated to \"rating.txt\"");
        System.out.println("Type \"!rating\" to get your current score");
        System.out.println("Type \"!help\" to get this message one more time");
    }
}
