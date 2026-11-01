from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print("Hello from ChatOpenAI")
    information= """
    Halloween,[a] also known as All Hallows' Eve[9] or All Saints' Eve,[10] is a celebration observed in many countries on 31 October, the eve of Western Christianity's feast of All Hallows' Day. It is at the beginning of the observance of Allhallowtide,[11] the time in the Christian liturgical year dedicated to remembering the dead, including saints (hallows), Christian martyrs, and all the faithful departed.[3][12][13] In popular culture, Halloween has become a celebration of horror and is associated with the macabre and the supernatural.[12][14]
    One theory holds that many Halloween traditions were influenced by Celtic harvest festivals, particularly the Gaelic festival Samhain, which is believed to have pagan roots.[15][16][17][18] Some theories go further and suggest that Samhain may have been Christianized as All Hallows' Day, along with its eve, by the Christian Church.[19][1][20] Other scholars say Halloween began independently as a Christian holiday, being the vigil of All Hallows' Day.[21][22][23] Celebrated in Ireland and Scotland for centuries, Irish and Scottish immigrants brought many Halloween customs to North America in the 19th century,[24][25] and then through American influence various Halloween customs spread to other countries by the late 20th and early 21st centuries
    """
    summary="""
    given the above information {information} about a person I want to create
    1. A Short Summary
    2. 2 interesting facts
    """
    summary_promt_template=PromptTemplate(
        input_variables=["information"], template=summary
        )
    llm=ChatOpenAI(temperature=0,model="gpt-5")
    chain=summary_promt_template | llm
    response=chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()