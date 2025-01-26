
/*
package frc.robot.subsystems;


//imports
import com.revrobotics.RelativeEncoder;
import com.revrobotics.CANSparkLowLevel.MotorType;

import java.util.function.DoubleSupplier;

import com.revrobotics.CANSparkMax;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.FunctionalCommand;
import edu.wpi.first.wpilibj2.command.SubsystemBase;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;


public class TankDriveSubsystem extends SubsystemBase{

  CANSparkMax leftDrive;
  CANSparkMax rightDrive;
  CANSparkMax leftDriveFollower;
  CANSparkMax rightDriveFollower;
  DifferentialDrive robotDrive;

  RelativeEncoder leftEncoder;
  RelativeEncoder rightEncoder;


  //constructor
  public TankDriveSubsystem()
  {

    leftDrive = new CANSparkMax(12, MotorType.kBrushless);
    leftDriveFollower = new CANSparkMax(10, MotorType.kBrushless);
    rightDrive = new CANSparkMax(11, MotorType.kBrushless);
    rightDriveFollower = new CANSparkMax(13, MotorType.kBrushless);

    leftEncoder = leftDrive.getEncoder();
    rightEncoder = rightDrive.getEncoder();

    robotDrive = new DifferentialDrive(leftDrive, rightDrive);

    leftDrive.restoreFactoryDefaults();
    leftDriveFollower.restoreFactoryDefaults();
    rightDrive.restoreFactoryDefaults();
    rightDriveFollower.restoreFactoryDefaults();
    
    leftEncoder.setPosition(0);
    rightEncoder.setPosition(0);

    leftDriveFollower.follow(leftDrive);
    rightDriveFollower.follow(rightDrive);

  }


  

  //when game controller button B is pressed change color to red
  public Command tankDrive(DoubleSupplier leftJoystick, DoubleSupplier rightJoystick)
  {
    return new FunctionalCommand(


      // ** INIT
      ()-> testInit1(),
     
      // ** EXECUTE
      ()-> {
        double leftValue = leftJoystick.getAsDouble()*-1;
        double rightValue = rightJoystick.getAsDouble();
        System.out.println(leftValue);
        System.out.println(rightValue);
        robotDrive.tankDrive(leftValue, rightValue);
      },
     
      // ** ON INTERRUPTED
      interrupted-> {
        robotDrive.tankDrive(0, 0);
      },
     
      // ** END CONDITION
      ()-> testEndCondition1(),


      // ** REQUIREMENTS
      this);


  }
  
  
  private void testInit1()
  {

  }


  private boolean testEndCondition1()
  {
    return(false);
  }

} */


