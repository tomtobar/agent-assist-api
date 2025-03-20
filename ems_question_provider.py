from faker.providers import BaseProvider

class EmsQuestionProvider(BaseProvider):
    __provider__ = "ems_question"

    def ems_question(self):
        contract_questions = [
            "How do I set the financial split for a student's contract?",
            "What are the steps to update the financial split after contract submission?",
            "Why is my financial split not updating in the ledger?",
            "Can I assign a financial split before the contract is signed?",
            "How can I adjust the financial split for multiple students in a household?",
            "What happens if no financial split is set before contract submission?",
            "How do I reassign the financial responsibility to another payer?",
            "Can a parent update their financial split percentage in the Billing Management tab?",
            "What happens to past contract charges when the financial split is changed?",
            "How does the financial split affect the ledger for future payments?",
            "Can I set different financial split percentages for siblings?",
            "What happens if a parent with a 0% financial split submits the contract?",
            "How do I export financial split data for all enrolled students?",
            "Can I override a financial split once a contract has been finalized?",
            "What should I do if a parent wants to make occasional payments without a financial split?",
            "How does the financial split carry over from year to year?",
            "Is it possible to manually adjust charges after modifying the financial split?",
            "What happens to the deposit charge if the financial split is changed after contract submission?",
            "Can I search for parents or guardians based on their financial split percentage?",
            "What happens to the ledger if the financial split is modified and the contract is re-submitted internally?"
        ]

    
        return self.random_element(contract_questions)
