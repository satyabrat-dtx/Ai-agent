# DB2ADMIN.SCDM_RULE_OCC_TO_OCC

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDM_')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `OO_IDENTIFIER`, `OO_WKCNTER`, `OO_RSC_CODE`, `OO_RES_CATEGORY`, `OO_WC_PROCESS`, `OO_PROPERTY`, `OO_TYPE_PROD`, `OO_LINE_NUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 186249

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `OO_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `OO_WKCNTER` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `OO_RSC_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `OO_RES_CATEGORY` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `OO_WC_PROCESS` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `OO_PROPERTY` | VARCHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `OO_TYPE_PROD` | VARCHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `OO_LINE_NUMBER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 8 | `OO_SEQUENCE` | SMALLINT | NOT NULL |  |  |  |
| 9 | `OO_DEP_ON_CURR` | CHAR(1) |  |  |  |  |
| 10 | `OO_DEP_VALUE` | VARCHAR(90) |  |  |  |  |
| 11 | `OO_RULE_CONST` | VARCHAR(90) |  |  |  |  |
| 12 | `OO_OPERAND` | VARCHAR(2) |  |  |  |  |
| 13 | `OO_CASE` | VARCHAR(2) |  |  |  |  |
| 14 | `OO_SETUP_TYPE` | CHAR(1) |  |  |  |  |
| 15 | `OO_SETUP_TIME` | DECIMAL(11,2) |  |  |  |  |
| 16 | `OO_SETUP_OVERLAPPING_TIME` | DECIMAL(11,2) |  |  |  |  |
| 17 | `OO_SETUP_TIME_MULT` | DECIMAL(9,4) |  |  |  |  |
| 18 | `OO_OVERLAPPING_TIME_MULT` | DECIMAL(9,4) |  |  |  |  |
| 19 | `OO_CAN_BE_SAME_GROUP` | CHAR(1) |  |  |  |  |
| 20 | `OO_TEORETIC_WC` | VARCHAR(8) |  |  |  |  |
| 21 | `OO_DURATION` | DECIMAL(11,2) |  |  |  |  |
| 22 | `OO_LEAD_TIME` | DECIMAL(11,2) |  |  |  |  |
| 23 | `OO_FROM_POS` | SMALLINT |  |  |  |  |
| 24 | `OO_LENGTH` | SMALLINT |  |  |  |  |
| 25 | `OO_PARTIAL_PROP_VAL` | CHAR(1) |  |  |  |  |
| 26 | `OO_NEXT_SEQ_WHEN_OK` | SMALLINT |  |  |  |  |
| 27 | `OO_NUM_OF_DEC` | SMALLINT |  |  |  |  |
| 28 | `OO_LEARNING_CURVE_CODE` | VARCHAR(6) |  |  |  |  |
| 29 | `OO_USR_NAMECR` | VARCHAR(10) |  |  |  |  |
| 30 | `OO_USR_TIMECR` | TIMESTAMP |  |  |  |  |
| 31 | `OO_USR_NAMECG` | VARCHAR(10) |  |  |  |  |
| 32 | `OO_USR_TIMECG` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.OO_IDENTIFIER,
       t.OO_WKCNTER,
       t.OO_RSC_CODE,
       t.OO_RES_CATEGORY,
       t.OO_WC_PROCESS,
       t.OO_PROPERTY,
       t.OO_TYPE_PROD,
       t.OO_LINE_NUMBER,
       t.OO_SEQUENCE,
       t.OO_DEP_ON_CURR,
       t.OO_DEP_VALUE,
       t.OO_RULE_CONST
FROM   DB2ADMIN.SCDM_RULE_OCC_TO_OCC t
FETCH FIRST 100 ROWS ONLY;
```
