# 🕒 Mr-Clock (Multi-Timezone Clock Application)

A simple and robust Python application that displays current time and date information across multiple timezones, featuring a license management system and modern UI. ⚡

<div align="center">
  
  [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mrjxtr)
  [![Upwork](https://img.shields.io/badge/-Upwork-6fda44?style=flat-square&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01f2fd0e74a0c5055a?mp_source=share)
  [![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/mrjxtr)
  [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/mrjxtr)
  [![Threads](https://img.shields.io/badge/-Threads-000000?style=flat-square&logo=threads&logoColor=white)](https://www.threads.net/@mrjxtr)
  [![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/mrjxtr)
  [![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:mr.jesterlumacad@gmail.com)

</div>

## ✨ Features

### 🎯 Core Features

- ⏰ Real-time display of local time and date
- 🌎 EST timezone display (licensed version)
- 🎨 Modern, responsive UI using CustomTkinter
- ⚙️ Configurable time and date formats

### 🔑 License Management

- ⏳ 30-day trial period with remaining days display
- 🔒 Secure machine-specific license activation
- 📊 Multiple license states (Trial, Licensed, Expired, Invalid)
- 🛡️ Graceful error handling and user feedback

### 🖥️ User Interface

- 🎯 Clean and intuitive interface
- 📱 Auto-adjusting window size
- ⚠️ Error message display with auto-dismiss
- 📌 Status indicators for license state
- ⚡ Responsive time updates

## 📋 Requirements

- 🐍 Python 3.8 or higher
- 💻 Operating System: Windows, macOS, or Linux

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/multi-timezone-clock.git
   cd multi-timezone-clock
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (for license testing):

   ```bash
   # Create .env file
   echo "LICENSE_KEY=DEMO-123-456-789" > .env
   ```

## 📖 Usage

### 🎮 Running the Application

```bash
python src/main.py
```

### 📝 License States

1. **🔄 Trial Version**

   - 🆕 Automatically starts with a 30-day trial
   - 🕒 Displays local time only
   - ⏳ Shows remaining trial days
   - 🔑 Includes license activation option

2. **✅ Licensed Version**

   - 🌎 Displays both local and EST time
   - 🔒 Machine-specific license validation
   - ⭐ Permanent access to all features

3. **❌ Expired/Invalid**
   - 🚫 Clear notification of license status
   - 🔑 Option to activate valid license
   - 🛡️ Graceful degradation of functionality

### 🔐 License Activation

1. During trial period:

   - 🖱️ Click the "Activate License" button
   - ⌨️ Enter your license key
   - ✅ System will validate and activate if valid

2. After expiration:
   - 🔄 Use the activation interface on the expired notice
   - 🔑 Enter a valid license key to restore functionality

## 📁 Project Structure

```plaintext
multi-timezone-clock/
├── src/
│   ├── main.py           # Application entry point
│   ├── ui/
│   │   ├── app.py        # Main application window
│   │   └── clock_display.py  # Clock display components
│   └── utils/
│       └── license_manager.py  # License management
├── requirements.txt      # Project dependencies
├── .env                 # Environment variables (create this)
└── README.md           # Project documentation
```

## 🛠️ Development

### 🧩 Key Components

- 🖥️ `App`: Main application window and UI management
- ⏰ `ClockDisplay`: Handles time display and timezone logic
- 🎯 `TimeFrame`: Individual time display component
- 🔑 `LicenseManager`: License validation and trial management

### ⚠️ Error Handling

The application includes comprehensive error handling:

- 🛡️ Graceful degradation on errors
- 💬 User-friendly error messages
- 📝 Logging of technical errors
- 🔄 Automatic recovery where possible

## 🧪 Testing

For testing the license system, use:

- 🔑 Demo Key: `DEMO-123-456-789`
- 🔄 Test different states by modifying the trial start date in `license_data.json`

## 🤝 Contributing

1. 🔀 Fork the repository
2. 🌿 Create a feature branch
3. ✍️ Commit your changes
4. 🚀 Push to the branch
5. 📬 Create a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- 🎨 CustomTkinter for the modern UI components
- ⏰ Python datetime and pytz for timezone management

## 📫 Let's Connect!

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mrjxtr)
[![Upwork](https://img.shields.io/badge/-Upwork-6fda44?style=flat-square&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01f2fd0e74a0c5055a?mp_source=share)
[![Facebook](https://img.shields.io/badge/-Facebook-1877F2?style=flat-square&logo=facebook&logoColor=white)](https://www.facebook.com/mrjxtr)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/mrjxtr)
[![Threads](https://img.shields.io/badge/-Threads-000000?style=flat-square&logo=threads&logoColor=white)](https://www.threads.net/@mrjxtr)
[![Twitter](https://img.shields.io/badge/-Twitter-1DA1F2?style=flat-square&logo=twitter&logoColor=white)](https://twitter.com/mrjxtr)
[![Gmail](https://img.shields.io/badge/-Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:mr.jesterlumacad@gmail.com)
