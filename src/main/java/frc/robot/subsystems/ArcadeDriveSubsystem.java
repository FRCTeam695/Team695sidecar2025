
/*
package frc.robot.subsystems;


//imports
import com.revrobotics.RelativeEncoder;
import com.revrobotics.CANSparkLowLevel.MotorType;

import java.util.function.DoubleSupplier;

import com.revrobotics.spark.SparkFlex;
import edu.wpi.first.wpilibj2.command.Command;
import edu.wpi.first.wpilibj2.command.FunctionalCommand;
import edu.wpi.first.wpilibj2.command.SubsystemBase;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;


public class ArcadeDriveSubsystem extends SubsystemBase{

  SparkFlex leftDrive;
  SparkFlex rightDrive;
  SparkFlex leftDriveFollower;
  SparkFlex rightDriveFollower;
  DifferentialDrive robotDrive;

  RelativeEncoder leftEncoder;
  RelativeEncoder rightEncoder;


  //constructor
  public ArcadeDriveSubsystem()
  {

    leftDrive = new SparkFlex(12, MotorType.kBrushless);
    leftDriveFollower = new SparkFlex(10, MotorType.kBrushless);
    rightDrive = new SparkFlex(11, MotorType.kBrushless);
    rightDriveFollower = new SparkFlex(13, MotorType.kBrushless);

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
  public Command arcadeDrive(DoubleSupplier leftForward, DoubleSupplier rightTwist)
  {
    return new FunctionalCommand(


      // ** INIT
      ()-> testInit1(),
     
      // ** EXECUTE
      ()-> {
        double forward = leftForward.getAsDouble();
        double turn = rightTwist.getAsDouble();
        System.out.println(forward);
        System.out.println(turn);
        robotDrive.arcadeDrive(forward, turn);
      },
     
      // ** ON INTERRUPTED
      interrupted-> {
        robotDrive.arcadeDrive(0, 0);
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

