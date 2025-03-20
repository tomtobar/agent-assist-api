from faker.providers import BaseProvider

class EmsQuestionProvider(BaseProvider):
    __provider__ = "ems_question"
    __provider__ = "ai_repsonse"

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
    
    def ai_response(self):
        contract_answers = [
            "To set the financial split, navigate to the Parent Portal Access tab in the student's record and enter the desired percentage for each guardian.",
            "You can update the financial split by going to the student's record, selecting the Parent Portal Access tab, and adjusting the percentages. These changes apply to future charges only.",
            "If the financial split is not updating in the ledger, ensure it was assigned before contract submission. Any changes made afterward will only apply to future charges.",
            "Yes, financial split percentages can be assigned before contract signing. If left blank, the system defaults to assigning 100% responsibility to the payer submitting the deposit.",
            "Each student’s financial split must be updated individually in their Parent Portal Access tab. There's no bulk update feature for multiple students in the same household.",
            "If no financial split is set before contract submission, the system assigns 100% responsibility to the payer who submits the deposit.",
            "To reassign financial responsibility, modify the financial split percentage in the Parent Portal Access tab. Future charges will update automatically, but past charges will remain unchanged.",
            "No, only administrators with financial permissions can modify financial split percentages. Parents cannot update this in the Billing Management tab.",
            "Past contract charges remain unchanged when the financial split is modified. Only future charges tied to the contract will reflect the new split.",
            "The financial split determines how future contract charges are divided among assigned payers. Each payer's ledger will update according to their assigned percentage.",
            "Yes, financial split percentages can be set individually for each sibling, allowing for different responsibilities within the same household.",
            "If a parent with a 0% financial split submits the contract, the assigned financial split remains unchanged. The responsible payer(s) will still be assigned based on the existing settings.",
            "You can export financial split data by navigating to Search & Reports, selecting 'Enrolled' students, and exporting the data as a Billing import template.",
            "Yes, financial split percentages can be overridden even after contract finalization. However, changes only apply to future charges and do not affect past payments.",
            "If a parent wants to make occasional payments without financial responsibility, assign them Shared Access. This allows them to log in and submit payments as needed.",
            "By default, financial split settings carry over from year to year. However, they can be updated annually if needed to reflect changes in responsibility.",
            "Yes, charges can be manually adjusted after modifying the financial split. However, these adjustments must be made separately, as financial split changes do not retroactively alter past charges.",
            "The deposit charge remains on the original payer’s ledger and is not affected by financial split changes after contract submission.",
            "You can search for parents or guardians based on their financial split percentage by exporting the Billing import template, which includes financial responsibility details.",
            "If the financial split is modified and the contract is re-submitted internally, future contract charges will be reassigned according to the new split, but past charges will remain unchanged."
        ]

        return self.random_element(contract_answers)


