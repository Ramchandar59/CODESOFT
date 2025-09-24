import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class WindowNotificationExamples {
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new WindowNotificationExamples().createMainWindow();
        });
    }
    
    private void createMainWindow() {
        JFrame frame = new JFrame("Notification Examples");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLocationRelativeTo(null);
        
        JPanel panel = new JPanel(new GridLayout(5, 1, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        
        // Button for basic dialog notification
        JButton dialogBtn = new JButton("Show Dialog Notification");
        dialogBtn.addActionListener(e -> showDialogNotification());
        
        // Button for toast-style notification
        JButton toastBtn = new JButton("Show Toast Notification");
        toastBtn.addActionListener(e -> showToastNotification());
        
        // Button for system tray notification (if supported)
        JButton trayBtn = new JButton("Show System Tray Notification");
        trayBtn.addActionListener(e -> showSystemTrayNotification());
        trayBtn.setEnabled(SystemTray.isSupported());
        
        // Button for custom popup notification
        JButton customBtn = new JButton("Show Custom Popup");
        customBtn.addActionListener(e -> showCustomPopup());
        
        // Button for slide-in notification
        JButton slideBtn = new JButton("Show Slide-in Notification");
        slideBtn.addActionListener(e -> showSlideInNotification());
        
        panel.add(dialogBtn);
        panel.add(toastBtn);
        panel.add(trayBtn);
        panel.add(customBtn);
        panel.add(slideBtn);
        
        frame.add(panel);
        frame.setVisible(true);
    }
    
    // Method 1: Basic Dialog Notification
    private void showDialogNotification() {
        JOptionPane.showMessageDialog(
            null,
            "This is a basic notification message!",
            "Notification",
            JOptionPane.INFORMATION_MESSAGE
        );
    }
    
    // Method 2: Toast-style Notification (auto-disappearing)
    private void showToastNotification() {
        JWindow toast = new JWindow();
        toast.setBackground(new Color(0, 0, 0, 0));
        
        JPanel panel = new JPanel();
        panel.setBackground(new Color(0, 0, 0, 200));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 20, 10, 20));
        
        JLabel label = new JLabel("Toast Notification - Will disappear in 3 seconds");
        label.setForeground(Color.WHITE);
        label.setFont(new Font("Arial", Font.BOLD, 12));
        
        panel.add(label);
        toast.add(panel);
        toast.pack();
        
        // Position at bottom right of screen
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        toast.setLocation(
            screenSize.width - toast.getWidth() - 20,
            screenSize.height - toast.getHeight() - 60
        );
        
        toast.setVisible(true);
        
        // Auto-hide after 3 seconds
        Timer timer = new Timer(3000, e -> toast.dispose());
        timer.setRepeats(false);
        timer.start();
    }
    
    // Method 3: System Tray Notification
    private void showSystemTrayNotification() {
        if (!SystemTray.isSupported()) {
            JOptionPane.showMessageDialog(null, "System tray is not supported!");
            return;
        }
        
        try {
            SystemTray tray = SystemTray.getSystemTray();
            
            // Create tray icon (using a simple colored image)
            Image image = createTrayIcon();
            TrayIcon trayIcon = new TrayIcon(image, "Java Notification App");
            trayIcon.setImageAutoSize(true);
            
            // Add to system tray
            tray.add(trayIcon);
            
            // Show notification
            trayIcon.displayMessage(
                "System Notification",
                "This is a system tray notification!",
                TrayIcon.MessageType.INFO
            );
            
            // Remove after 5 seconds
            Timer timer = new Timer(5000, e -> tray.remove(trayIcon));
            timer.setRepeats(false);
            timer.start();
            
        } catch (AWTException e) {
            e.printStackTrace();
        }
    }
    
    // Method 4: Custom Popup Window
    private void showCustomPopup() {
        JWindow popup = new JWindow();
        popup.setAlwaysOnTop(true);
        
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBackground(new Color(70, 130, 180));
        panel.setBorder(BorderFactory.createCompoundBorder(
            BorderFactory.createLineBorder(Color.DARK_GRAY, 2),
            BorderFactory.createEmptyBorder(15, 15, 15, 15)
        ));
        
        JLabel titleLabel = new JLabel("Custom Notification", SwingConstants.CENTER);
        titleLabel.setFont(new Font("Arial", Font.BOLD, 14));
        titleLabel.setForeground(Color.WHITE);
        
        JLabel messageLabel = new JLabel("Click anywhere to close this notification");
        messageLabel.setFont(new Font("Arial", Font.PLAIN, 12));
        messageLabel.setForeground(Color.WHITE);
        messageLabel.setHorizontalAlignment(SwingConstants.CENTER);
        
        panel.add(titleLabel, BorderLayout.NORTH);
        panel.add(messageLabel, BorderLayout.CENTER);
        
        // Add click listener to close
        panel.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                popup.dispose();
            }
        });
        
        popup.add(panel);
        popup.setSize(300, 100);
        
        // Center on screen
        popup.setLocationRelativeTo(null);
        popup.setVisible(true);
    }
    
    // Method 5: Slide-in Notification
    private void showSlideInNotification() {
        JWindow slideWindow = new JWindow();
        slideWindow.setAlwaysOnTop(true);
        
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBackground(new Color(46, 125, 50));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 15, 10, 15));
        
        JLabel label = new JLabel("Slide-in Notification!");
        label.setForeground(Color.WHITE);
        label.setFont(new Font("Arial", Font.BOLD, 13));
        
        JButton closeBtn = new JButton("×");
        closeBtn.setPreferredSize(new Dimension(25, 25));
        closeBtn.setBackground(new Color(76, 155, 80));
        closeBtn.setForeground(Color.WHITE);
        closeBtn.setBorder(null);
        closeBtn.setFocusPainted(false);
        closeBtn.addActionListener(e -> slideWindow.dispose());
        
        panel.add(label, BorderLayout.CENTER);
        panel.add(closeBtn, BorderLayout.EAST);
        
        slideWindow.add(panel);
        slideWindow.pack();
        
        // Start position (off-screen right)
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int finalX = screenSize.width - slideWindow.getWidth() - 20;
        int finalY = 50;
        
        slideWindow.setLocation(screenSize.width, finalY);
        slideWindow.setVisible(true);
        
        // Animate slide-in
        Timer slideTimer = new Timer(10, new ActionListener() {
            int currentX = screenSize.width;
            
            @Override
            public void actionPerformed(ActionEvent e) {
                currentX -= 8;
                if (currentX <= finalX) {
                    currentX = finalX;
                    ((Timer) e.getSource()).stop();
                    
                    // Auto-hide after 4 seconds
                    Timer hideTimer = new Timer(4000, evt -> {
                        // Animate slide-out
                        Timer slideOutTimer = new Timer(10, new ActionListener() {
                            int x = finalX;
                            @Override
                            public void actionPerformed(ActionEvent e) {
                                x += 8;
                                slideWindow.setLocation(x, finalY);
                                if (x >= screenSize.width) {
                                    ((Timer) e.getSource()).stop();
                                    slideWindow.dispose();
                                }
                            }
                        });
                        slideOutTimer.start();
                    });
                    hideTimer.setRepeats(false);
                    hideTimer.start();
                }
                slideWindow.setLocation(currentX, finalY);
            }
        });
        slideTimer.start();
    }
    
    // Helper method to create a simple tray icon
    private Image createTrayIcon() {
        int size = 16;
        BufferedImage image = new BufferedImage(size, size, BufferedImage.TYPE_INT_ARGB);
        Graphics2D g2d = image.createGraphics();
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2d.setColor(new Color(70, 130, 180));
        g2d.fillOval(0, 0, size, size);
        g2d.setColor(Color.WHITE);
        g2d.fillOval(size/4, size/4, size/2, size/2);
        g2d.dispose();
        return image;
    }
}
