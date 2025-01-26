// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

package frc.robot;

import java.lang.Object;
import frc.robot.Constants.OperatorConstants;
import frc.robot.commands.Autos;
import frc.robot.subsystems.ExampleSubsystem;
import frc.robot.subsystems.LEDSubsystem;
//import frc.robot.subsystems.MotorSubsystem;
import frc.robot.subsystems.ServoSubsystem;
//import frc.robot.subsystems.TankDriveSubsystem;
//import frc.robot.subsystems.ArcadeDriveSubsystem;
//import frc.robot.subsystems.SwerveSubsystem;
//import frc.robot.subsystems.SwerveModule;

import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.Commands;
import edu.wpi.first.wpilibj2.command.button.CommandGenericHID;
import edu.wpi.first.wpilibj2.command.button.CommandXboxController;
import edu.wpi.first.wpilibj2.command.button.Trigger;

/**
 * This class is where the bulk of the robot should be declared. Since Command-based is a
 * "declarative" paradigm, very little robot logic should actually be handled in the {@link Robot}
 * periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
 * subsystems, commands, and trigger mappings) should be declared here.
 */
public class RobotContainer {
  // The robot's subsystems and commands are defined here...
  private final ExampleSubsystem m_exampleSubsystem = new ExampleSubsystem();
  //private final LEDSubsystem m_LEDSubsystem = new LEDSubsystem();
  //private final ServoSubsystem m_ServoSubsystem = new ServoSubsystem();
  //private final MotorSubsystem m_motorSubsystem = new MotorSubsystem();
  //private final TankDriveSubsystem tankDriveSubsystem = new TankDriveSubsystem();
  //private final ArcadeDriveSubsystem arcadeDriveSubsystem = new ArcadeDriveSubsystem();
  //private final SwerveSubsystem swerveSubsystem = new SwerveSubsystem(50, 50);

  // Replace with CommandPS4Controller or CommandJoystick if needed
  public static CommandXboxController m_driverController = new CommandXboxController(OperatorConstants.kDriverControllerPort);


  public static CommandGenericHID m_joystickLeft = new CommandGenericHID(0);
  public static CommandGenericHID m_joystickRight = new CommandGenericHID(1);



  /** The container for the robot. Contains subsystems, OI devices, and commands. */
  public RobotContainer() {
    // Configure the trigger bindings
    configureBindings();
    
  }

  /**
   * Use this method to define your trigger->command mappings. Triggers can be created via the
   * {@link Trigger#Trigger(java.util.function.BooleanSupplier)} constructor with an arbitrary
   * predicate, or via the named factories in {@link
   * edu.wpi.first.wpilibj2.command.button.CommandGenericHID}'s subclasses for {@link
   * CommandXboxController Xbox}/{@link edu.wpi.first.wpilibj2.command.button.CommandPS4Controller
   * PS4} controllers or {@link edu.wpi.first.wpilibj2.command.button.CommandJoystick Flight
   * joysticks}.
   */
  private void configureBindings() {
    // Schedule `exampleMethodCommand` when the Xbox controller's B button is pressed,
    // cancelling on release.
  
    //m_driverController.b().toggleOnTrue(m_exampleSubsystem.redLEDCommand());
    //m_driverController.a().toggleOnTrue(m_exampleSubsystem.greenLEDCommand());
    //m_driverController.x().whileTrue(m_exampleSubsystem.runServoC(() -> m_driverController.getRawAxis(1)));
    //m_driverController.y().whileTrue(m_exampleSubsystem.servoToLED(() -> m_driverController.getRawAxis(1)));
    //m_driverController.leftBumper().onTrue(m_exampleSubsystem.runServoCC(5));
    //m_driverController.x().toggleOnTrue(m_motorSubsystem.runMotor(() -> m_driverController.getRawAxis(1)));
    //m_driverController.b().onTrue(m_motorSubsystem.buttonLimitSwitch());
    //tankDriveSubsystem.setDefaultCommand(tankDriveSubsystem.tankDrive(() -> m_joystickLeft.getRawAxis(1), () -> m_joystickRight.getRawAxis(1)));
    //tankDriveSubsystem.setDefaultCommand(arcadeDriveSubsystem.arcadeDrive(() -> m_joystickLeft.getRawAxis(1), () -> m_joystickRight.getRawAxis(1)));
    //swerveSubsystem.setDefaultCommand(swerveSubsystem.drive(() -> m_driverController.getRawAxis(1),
    //() -> m_driverController.getRawAxis(0),
    //() -> m_driverController.getRawAxis(4)));
  }



  /**
   * Use this to pass the autonomous command to the main {@link Robot} class.
   *
   * @return the command to run in autonomous
  */
  public Command getAutonomousCommand() {
    // An example command will be run in autonomous
    return Autos.exampleAuto(m_exampleSubsystem);
  }
  
}
