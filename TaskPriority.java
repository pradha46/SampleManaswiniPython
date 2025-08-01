import java.util.PriorityQueue;

// Task class representing a task with a priority
class Task implements Comparable<Task> {
    private String name;
    private int priority;

    // Constructor to initialize task name and priority
    public Task(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    // Getter method for task name
    public String getName() {
        return name;
    }

    // Getter method for task priority
    public int getPriority() {
        return priority;
    }

    // Implementation of compareTo method from Comparable interface
    // Allows tasks to be compared based on their priority
    @Override
    public int compareTo(Task other) {
        return Integer.compare(this.priority, other.priority);
    }

    // Override toString method for better task representation
    @Override
    public String toString() {
        return "Task{" +
                "name='" + name + '\'' +
                ", priority=" + priority +
                '}';
    }
}

// TaskScheduler class implementing priority-based task scheduling
class TaskScheduler 
{
    private PriorityQueue<Task> taskQueue;

    // Constructor to initialize PriorityQueue for task scheduling
    public TaskScheduler() 
    {
        // Initialize the priority queue with a comparator for task priority
        taskQueue = new PriorityQueue<>();
    }

    // Method to add a new task to the scheduler
    public void addTask(Task task) {
        taskQueue.offer(task); // Adds task to the priority queue
    }

    // Method to retrieve and execute the highest priority task
    public void executeNextTask() {
        Task task = taskQueue.poll(); // retrieves and removes the highest priority task
        if (task != null) {
            System.out.println("Executing task: " + task.getName()); 
        } else {
            System.out.println("No tasks left to execute."); 
        }
    }
}

// main class demonstrating the usage of TaskScheduler
public class PriorityTaskSchedulerExample {
    public static void main(String[] args) {
        TaskScheduler scheduler = new TaskScheduler(); // creates an instance of TaskScheduler

        // adding tasks with different priorities
        scheduler.addTask(new Task("Task 1", 3));
        scheduler.addTask(new Task("Task 2", 1));
        scheduler.addTask(new Task("Task 3", 2));

        // executing tasks in priority order
        scheduler.executeNextTask(); // Task 2 (highest priority)
        scheduler.executeNextTask(); // Task 3
        scheduler.executeNextTask(); // Task 1
        scheduler.executeNextTask(); // No tasks left
    }
}
