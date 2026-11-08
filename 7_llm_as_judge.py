from LLMcalls import chat_ollama
import unittest


##################################################################
# A FUNCTION THAT (HOPEFULLY) RETURNS THE CAPITAL OF ANY COUNTRY #
##################################################################

def ask_capital(country, model="gemma4"):
    prompt = f"What is the capital of {country}?"
    response = chat_ollama(model, prompt, verbose=False)
    return response['message']['content']


################################
# SOME TESTS FOR THAT FUNCTION #
################################

# HELPER FUNCTION FOR LLM AS JUDGE, RETURNS TRUE OR FALSE
def llm_as_a_judge_agrees(country, answer, expected):
    prompt = (f"Question: What is the capital of {country}?\n"
              f"Expected answer: {expected}\n"
              f"Given answer: {answer}\n\n"
              f"Does the given answer agree with the expected answer? "
              f"Extra details are fine as long as they do not contradict it. Reply with only YES or NO.")
    verdict = chat_ollama("gemma4", prompt, verbose=False)['message']['content']
    return verdict.strip().upper().startswith("YES")


###################################################################################
# TESTING HAPPENS HERE (THEY SHOULD NOT BE HERE, BUT THAT IS NOT OUR FOCUS TODAY) #
###################################################################################

class TestApp(unittest.TestCase):

    # WRONG MODEL
    def test_unknown_model_returns_failure(self):
        response = ask_capital("Sweden", "no-such-model")
        self.assertEqual(response, "Failure.")

    # CONSISTENCY TEST
    def test_knows_capital_of_sweden(self):
        correct = 0
        for i in range(3):
            answer = ask_capital("Sweden")
            if "Stockholm" in answer:
                correct += 1
        self.assertGreaterEqual(correct, 2)

    # LLM AS JUDGE
    def test_judge_accepts_right_capital(self):
        answer = "The capital of Sweden is Stockholm."
        self.assertTrue(llm_as_a_judge_agrees("Sweden", answer, "Stockholm"))

    # HALLUCINATIONS
    def test_judge_rejects_invented_capital(self):
        answer = "The capital of Bealandia is Bea City."
        self.assertFalse(llm_as_a_judge_agrees("Bealandia", answer, "There is no such country, so it has no capital."))


#############################
# RUN MAIN TO RUN THE TESTS #
#############################

if __name__ == "__main__":
    unittest.main()
