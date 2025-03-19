from setuptools import setup, find_packages

setup(
    name="cold_email_gen",  # Replace with your actual project name
    version="1.0.0",  # Update version as needed
    author="Gautam Aggarwal",  # Your name or organization
    author_email="gautam.aggarwal.tech@gmail.com",  # Your email
    description="This tool helps you to generate a email for job applications",
    long_description=open("README.md", encoding="utf-8").read(),    # Reads from README.md
    long_description_content_type="text/markdown",
    url="https://github.com/gautamaggarwaldev/Cold-Email-Generator.git",  # Your project repo
    packages=find_packages(),  # Automatically finds packages
    install_requires=[
        "streamlit",
        "langchain",
        "pandas",
        "chromadb",
        "dotenv",
        "uuid",
        "langchain_groq",
        "json"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Update if different
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
# streamlit run "v:\Langchain Projects\cold-email-gen\app.py"