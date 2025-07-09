import pytest
from analyzer.stress import get_word_stress, get_line_stress


class TestPOSVariants:
    """Test cases for POS-based pronunciation variant selection"""
    
    def test_record_as_noun(self):
        """Test 'record' as noun should have stress pattern [0, 1]"""
        # Context patterns that indicate noun usage
        contexts = [
            "the record shows",
            "a record of events", 
            "this record is important",
            "medical records are"
        ]
        
        for context in contexts:
            # This will fail until we implement POS detection
            # Expected: [0, 1] for noun "record"
            stress = get_word_stress("record", context)
            # TODO: assert stress == [0, 1] when implemented
    
    def test_record_as_verb(self):
        """Test 'record' as verb should have stress pattern [1, 0]"""
        contexts = [
            "I will record the meeting",
            "please record this",
            "they record everything", 
            "to record a song"
        ]
        
        for context in contexts:
            # Expected: [1, 0] for verb "record"
            stress = get_word_stress("record", context)
            # TODO: assert stress == [1, 0] when implemented
    
    def test_present_as_noun(self):
        """Test 'present' as noun should have stress pattern [1, 0]"""
        contexts = [
            "the present situation",
            "a present for you",
            "this present is nice",
            "Christmas presents"
        ]
        
        for context in contexts:
            stress = get_word_stress("present", context)
            # TODO: assert stress == [1, 0] when implemented
    
    def test_present_as_verb(self):
        """Test 'present' as verb should have stress pattern [0, 1]"""
        contexts = [
            "I will present the findings",
            "please present your work",
            "they present evidence",
            "to present a case"
        ]
        
        for context in contexts:
            stress = get_word_stress("present", context)
            # TODO: assert stress == [0, 1] when implemented
    
    def test_object_as_noun(self):
        """Test 'object' as noun should have stress pattern [1, 0]"""
        contexts = [
            "the object on the table",
            "a strange object",
            "this object is heavy"
        ]
        
        for context in contexts:
            stress = get_word_stress("object", context)
            # TODO: assert stress == [1, 0] when implemented
    
    def test_object_as_verb(self):
        """Test 'object' as verb should have stress pattern [0, 1]"""
        contexts = [
            "I object to this",
            "they object strongly",
            "we object to the proposal"
        ]
        
        for context in contexts:
            stress = get_word_stress("object", context)
            # TODO: assert stress == [0, 1] when implemented
    
    def test_contract_as_noun(self):
        """Test 'contract' as noun should have stress pattern [1, 2]"""
        contexts = [
            "the contract is valid",
            "sign the contract",
            "a legal contract"
        ]
        
        for context in contexts:
            stress = get_word_stress("contract", context)
            # TODO: assert stress == [1, 2] when implemented
    
    def test_contract_as_verb(self):
        """Test 'contract' as verb should have stress pattern [0, 1]"""
        contexts = [
            "muscles contract quickly",
            "they contract the work",
            "to contract a disease"
        ]
        
        for context in contexts:
            stress = get_word_stress("contract", context)
            # TODO: assert stress == [0, 1] when implemented
    
    def test_refuse_as_noun(self):
        """Test 'refuse' as noun should have stress pattern [1, 2]"""
        contexts = [
            "the refuse pile",
            "collect the refuse",
            "organic refuse"
        ]
        
        for context in contexts:
            stress = get_word_stress("refuse", context)
            # TODO: assert stress == [1, 2] when implemented
    
    def test_refuse_as_verb(self):
        """Test 'refuse' as verb should have stress pattern [0, 1]"""
        contexts = [
            "I refuse to go",
            "they refuse help",
            "we refuse the offer"
        ]
        
        for context in contexts:
            stress = get_word_stress("refuse", context)
            # TODO: assert stress == [0, 1] when implemented
    
    def test_produce_as_noun(self):
        """Test 'produce' as noun should have stress pattern [1, 0]"""
        contexts = [
            "fresh produce section",
            "buy local produce",
            "organic produce"
        ]
        
        for context in contexts:
            stress = get_word_stress("produce", context)
            # TODO: assert stress == [1, 0] when implemented
    
    def test_produce_as_verb(self):
        """Test 'produce' as verb should have stress pattern [0, 1]"""
        contexts = [
            "they produce cars",
            "to produce results",
            "we produce software"
        ]
        
        for context in contexts:
            stress = get_word_stress("produce", context)
            # TODO: assert stress == [0, 1] when implemented
    
    def test_fallback_to_original_behavior(self):
        """Test that words without POS variants fall back to original behavior"""
        # Test with a word that doesn't have noun/verb variants
        stress = get_word_stress("hello")
        assert stress is not None
        assert isinstance(stress, list)
        assert all(isinstance(s, int) for s in stress)
    
    def test_unknown_word_still_returns_none(self):
        """Test that unknown words still return None"""
        stress = get_word_stress("asdkfjhasd", "the asdkfjhasd is here")
        assert stress is None
    
    def test_pos_hint_parameter(self):
        """Test explicit POS hint parameter"""
        # This will test the pos_hint parameter when implemented
        # stress = get_word_stress("record", pos_hint="noun")
        # assert stress == [0, 1]
        
        # stress = get_word_stress("record", pos_hint="verb") 
        # assert stress == [1, 0]
        pass
    
    def test_line_stress_with_pos_variants(self):
        """Test that line stress analysis works with POS variants"""
        # Test a line with multiple POS-ambiguous words
        line = "I will record the present situation"
        result = get_line_stress(line)
        
        # Should have entries for each word
        assert len(result) == 5  # I, will, record, the, present, situation
        assert all('word' in entry and 'stress' in entry for entry in result)
        
        # TODO: When implemented, verify correct stress patterns:
        # "record" should be [1, 0] (verb)
        # "present" should be [1, 0] (noun/adjective)


class TestContextDetection:
    """Test cases for context-based POS detection"""
    
    def test_noun_indicators(self):
        """Test patterns that indicate noun usage"""
        noun_contexts = [
            ("the record", "record"),
            ("a present", "present"), 
            ("an object", "object"),
            ("this contract", "contract"),
            ("that refuse", "refuse"),
            ("these records", "record"),
            ("those presents", "present")
        ]
        
        # These tests will be enabled when context detection is implemented
        # for context, word in noun_contexts:
        #     pos = detect_pos_simple(word, context)
        #     assert pos == "noun", f"Expected noun for '{word}' in '{context}'"
    
    def test_verb_indicators(self):
        """Test patterns that indicate verb usage"""
        verb_contexts = [
            ("I record", "record"),
            ("will present", "present"),
            ("they object", "object"), 
            ("to contract", "contract"),
            ("we refuse", "refuse"),
            ("you produce", "produce"),
            ("he records", "record"),
            ("she presents", "present")
        ]
        
        # These tests will be enabled when context detection is implemented
        # for context, word in verb_contexts:
        #     pos = detect_pos_simple(word, context)
        #     assert pos == "verb", f"Expected verb for '{word}' in '{context}'"
    
    def test_ambiguous_contexts(self):
        """Test contexts where POS is unclear"""
        ambiguous_contexts = [
            ("record something", "record"),  # Could be noun or verb
            ("present here", "present"),     # Could be noun/adj or verb
            ("object there", "object")       # Could be noun or verb
        ]
        
        # These should fall back to default behavior
        # for context, word in ambiguous_contexts:
        #     pos = detect_pos_simple(word, context)
        #     assert pos == "unknown", f"Expected unknown for '{word}' in '{context}'"


class TestEdgeCases:
    """Test edge cases and error conditions"""
    
    def test_empty_context(self):
        """Test behavior with empty context"""
        stress = get_word_stress("record", "")
        # Should fall back to original behavior
        assert stress is not None
    
    def test_none_context(self):
        """Test behavior with None context"""
        stress = get_word_stress("record", None)
        # Should fall back to original behavior
        assert stress is not None
    
    def test_punctuation_handling(self):
        """Test that punctuation is handled correctly"""
        contexts = [
            ("the record.", "record"),
            ("I record,", "record"),
            ("present!", "present"),
            ("object?", "object")
        ]
        
        for context, word in contexts:
            stress = get_word_stress(word, context)
            assert stress is not None
    
    def test_case_insensitivity(self):
        """Test that case doesn't matter"""
        contexts = [
            ("The RECORD shows", "RECORD"),
            ("I Will PRESENT", "PRESENT"),
            ("they Object", "Object")
        ]
        
        for context, word in contexts:
            stress = get_word_stress(word, context)
            assert stress is not None