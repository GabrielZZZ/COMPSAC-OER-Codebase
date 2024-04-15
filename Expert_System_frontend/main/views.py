import json
from django.shortcuts import render, redirect
from django.conf import settings
from .models import QuizQuestion


# Page 1: Display Welcome message
def welcome(request):
    return render(request, 'welcome.html')

# Page 2: Display Menu message
def menu(request):
    return render(request, 'menuPage.html')

def standard_scenario_introduction(request):
    

    return render(request, 'standard_scenario_introduction.html')

def standard_scenario_structure(request):
    

    return render(request, 'standard_scenario_structure.html')



# Page 2: Display Menu message
def ads_introduction(request):
    welcome_message = "Welcome to the instruction page of this system. You will be provided with a background knowlege with Metamorphic Testing and Autonomous Driving vehicles."

    scenario_details = [
        {
            "title": "Basic structure of the scenario",
            "content": [
                "Scenario Format: Prefix: 'In the source scenario'",
                "Explanation: This is the introductory statement that sets the context for the scenario.",
                "Actor Initialization + Environment Information / ADS Infrastructure with Special Features:",
                "Explanation: Describe the initial conditions of the scenario, including the setup of actors and any relevant environmental details.",
                "Example: 'spawn the EGO vehicle near a parking slot with four poles at the corner'",
                # ... other details
            ],
        },
        # ... other sections
    ]

    prompts = [
        "Provide any other actors (vehicles/pedestrians) involved in the scenario in addition to the EGO vehicle (default), press 'n' if there is only ego vehicle in the scenario",
        "Provide the key simulation environment/ADS Infrastructures in the scenario (in a phrase). E.g., at a junction, near a parking slot.: User Answer: a pedestrian",
        "Describe what initial actions the actors in the scenario should take (in a complete sentence), e.g., 'The EGO vehicle drives behind the front vehicle V1.'",
        "Provide additional details or constraints that may impact the scenario's outcome (in a complete sentence), e.g., 'The front vehicle V1 slows down.'",
        "Describe the expected results or consequences of the scenario (in a complete sentence), e.g., 'The EGO vehicle slows down as well.'",
        # ... other prompts
    ]

 

    ads_introduction = """
Picture a car that can drive itself, just like the ones you see in science fiction movies. Well, guess what? It's not science fiction anymore; it's becoming a reality, and it's called "Autonomous Driving."

An autonomous driving vehicle, or self-driving car, is like having your very own robot chauffeur. Instead of a human driver, it uses smart sensors, cameras, and super-fast computers to navigate and make driving decisions all on its own. Yep, no hands on the steering wheel!

Here's how it works: These self-driving cars have a ton of sensors and cameras all around them. They "see" the road, other cars, pedestrians, and even traffic lights. These sensors collect a crazy amount of data, like a super-smart detective gathering clues.

Then, the car's brain, which is basically a supercomputer, analyzes all this data in real-time. It figures out where the car is, what's around it, and decides when to speed up, slow down, or stop. It can even change lanes and park itself, all without a human doing a thing!

Why is this so exciting? Well, first, it can make our roads safer. Computers don't get tired or distracted like humans do, so they can reduce accidents caused by human error. Plus, it can make driving more convenient. Imagine sitting back, relaxing, or getting work done while your car takes care of the driving.

Autonomous driving isn't just for cars; it's also for trucks, buses, and even delivery vehicles. It's like having a whole fleet of smart vehicles working together to make transportation smoother and more efficient.

Of course, it's not without its challenges. Engineers and scientists are working hard to make sure these self-driving vehicles are super safe and can handle tricky situations like bad weather or unusual road conditions.

So, whether you're excited about the future of transportation or just curious about how these amazing machines work, autonomous driving vehicles are changing the way we get around, making our roads safer and more convenient.
"""

    


    # Update context dictionary
    context = {
        'welcome_message': welcome_message,
        'scenario_details': scenario_details,
        'prompts': prompts,
        'ads_introduction': ads_introduction,

    }

    return render(request, 'ads_introduction.html', context)



# Page 2: Instruction Page
def instruction(request):
    welcome_message = "Welcome to the instruction page of this system. You will be provided with a background knowlege with Metamorphic Testing and Autonomous Driving vehicles."

    
    # New content for additional sections
    metamorphic_testing_intro = """
Imagine you're testing a self-driving car. You want to make sure it can navigate safely in various situations, from busy city streets to quiet rural roads. But testing such a complex system can be really challenging. This is where Metamorphic Testing comes to the rescue!

Metamorphic Testing is like having a superpower in software testing. Instead of checking if the car makes perfect decisions in every single scenario (which is almost impossible), we focus on how it behaves when we change something. We use "metamorphic relations" to describe these changes.

Think of metamorphic relations as rules that the car must follow no matter what. For example, one rule might be "if the car is in a lane, it should stay in that lane." Another could be "if it detects an obstacle, it must slow down or stop."

Here's the magic: we don't just test the car in one scenario; we test it in many scenarios. Each time, we change something, but we keep our metamorphic relations intact. For instance, we might test how the car behaves when there are more cars on the road or when it's raining heavily.

Metamorphic Testing helps us catch bugs that might slip through traditional testing. It's like having a bunch of friends who double-check your work by changing things and making sure everything still makes sense.

So, if you're into making software better and safer, Metamorphic Testing is a cool technique to explore. It's like a superhero sidekick for software testers, helping us ensure that complex systems like self-driving cars work reliably in a changing world.
"""

   

    # Update context dictionary
    context = {
        'welcome_message': welcome_message,
        'metamorphic_testing_intro': metamorphic_testing_intro
        
    }

    return render(request, 'instructionPage.html', context)

# Page 2: Display Menu message
def mrp_intro(request):
    welcome_message = "Welcome to the instruction page of this system. You will be provided with a background knowlege with Metamorphic Testing and Autonomous Driving vehicles."

    

    metamorphic_relation_patterns_tutorial = """
Think of Metamorphic Relation Patterns (MRPs) as the blueprint or recipe for creating smart rules, called Metamorphic Relations (MRs), that can supercharge your software testing. These patterns help you design the rules that your testing system will follow to uncover hidden issues and make sure your software behaves correctly.

Here's how it works:

    1. Designing Smart Rules: MRPs are like the artist's palette, giving you the colors to paint your testing canvas. They guide you in creating MRs, which are specific rules that describe how your software should behave when its inputs are transformed. For example, if you're testing a calculator, an MRP might help you design an MR that says, "When you add any two numbers, it shouldn't matter what order you add them in."
    
    2. Unleashing Testing Power: Once you've crafted MRs using MRPs, your testing system follows these rules automatically. It applies different transformations to your software's inputs, like changing the order of numbers or adjusting values, while making sure the fundamental logic stays intact.

    3. Detecting Hidden Bugs: MRPs are your secret weapon against sneaky bugs. By creating MRs based on well-thought-out patterns, you can uncover issues that might go unnoticed in regular testing. It's like having a detective who knows exactly where to look for clues.

    4. Enhancing Software Quality: MRPs contribute to the overall quality and reliability of your software. They ensure that your program behaves consistently and correctly under various conditions and transformations, making it more robust and trustworthy.

In summary, Metamorphic Relation Patterns (MRPs) are the tools you use to craft the rules (Metamorphic Relations or MRs) that power your software testing. They help you uncover hidden issues, improve software quality, and ensure that your program behaves as expected, even under different inputs and transformations. So, if you're into making software better and more reliable, MRPs are your creative toolkit for testing success!
"""


    # Update context dictionary
    context = {
        'welcome_message': welcome_message,
        
        
        'metamorphic_relation_patterns_tutorial': metamorphic_relation_patterns_tutorial,
    }

    return render(request, 'metamorphic_relation_patterns_tutorial.html', context)

# Page 2: Display Menu message
def mr_generation_tutorial(request):
    
    welcome_message = "Welcome to the instruction page of this system. You will be provided with a background knowlege with Metamorphic Testing and Autonomous Driving vehicles."

    mr_generation_tutorial = """
Imagine you're trying to make sure a computer program is working correctly. It could be a simple calculator or a complex piece of software. You want to test it thoroughly to catch any hidden errors. This is where Metamorphic Relations (MRs) come into play, and they're like special rules that help you test smarter.

An MR is like a friendly helper that tells you how things should change when you feed your program some input. Let's say you have a program that adds two numbers together. An MR could be something like, "If you add 5 and 3, the result should be the same as adding 3 and 5." This simple rule helps you check if the program follows the basic rules of addition.

Here's the cool part: you don't just test the program once. You test it multiple times, following your MRs each time. For our addition program, you might test it by swapping the numbers, by adding 0 to any number (which should give you the same number), or by doubling the numbers.

MR generation is the process of coming up with these smart rules. It's like making a list of instructions for testing. The better your MRs, the more thorough your testing becomes, and the more likely you are to catch sneaky bugs.

So, if you're interested in quality assurance and making sure software works correctly, MR generation is your secret weapon. It's all about creating rules that help you test software in a structured and efficient way. It's like having a playbook for testing, ensuring your software is reliable and bug-free.
"""

     # Update context dictionary
    context = {
        'welcome_message': welcome_message,
        
        'mr_generation_tutorial': mr_generation_tutorial,
        
    }
    
    return render(request, 'mr_generation_tutorial.html', context)




# Page 2: Choose from Database
def choose_scenario(request):
    # This view now simply renders the choose_scenario.html template.
    # The actual scenarios are loaded via JavaScript from the Flask backend.
    
    # Get the IP_ADDRESS from settings.py
    ip_address = settings.IP_ADDRESS
    
    return render(request, 'choose_scenario.html', {'ip_address': ip_address})


# Page 3.xxx: Question Pages
def questions(request):
    # This view now simply renders the choose_scenario.html template.
    # The actual scenarios are loaded via JavaScript from the Flask backend.
    
    # Get the IP_ADDRESS from settings.py
    ip_address = settings.IP_ADDRESS
    
    return render(request, 'questions.html',{'ip_address': ip_address})


# Page 4: Display MRs
def results(request):
    return render(request, 'results.html')

# Page 5: Display MRs
def mr_generation_template(request):
    return render(request, 'mr_generation_template.html')

def scenario_resultPage(request):
    return render(request, 'scenario_resultPage.html')
    
    

def quiz_view(request):
    
    return render(request, 'quiz.html')