# DB2ADMIN.SCDA_NOW_PROGRESS

- **Module**: `SCHEDULING` (high confidence — table name starts with 'SCDA_')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `NP_IDENTIFIER`, `NP_PROGRESS_NUMBER`, `NP_DEMAND_COUNTER_CODE`, `NP_DEMAND_CODE`, `NP_DEMAND_STEP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 184467

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NP_IDENTIFIER` | SMALLINT | NOT NULL | PK | primary_key |  |
| 1 | `NP_PROGRESS_NUMBER` | VARCHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `NP_PROGRESS_TAMPLATECODE` | VARCHAR(3) |  |  |  |  |
| 3 | `NP_DEMAND_COUNTER_CODE` | VARCHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `NP_DEMAND_CODE` | VARCHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `NP_DEMAND_STEP` | SMALLINT | NOT NULL | PK | primary_key |  |
| 6 | `NP_DEMAND_TEMPLATE_CODE` | VARCHAR(3) |  |  |  |  |
| 7 | `NP_PRODUCTION_ORDER_CODE` | VARCHAR(16) |  |  |  |  |
| 8 | `NP_ORIG_END_DATE` | TIMESTAMP |  |  |  |  |
| 9 | `NP_START_DATE_TIME` | TIMESTAMP |  |  |  |  |
| 10 | `NP_END_DATE_TIME` | TIMESTAMP |  |  |  |  |
| 11 | `NP_RESOURCE_CODE` | VARCHAR(8) |  |  |  |  |
| 12 | `NP_PRIMARY_QTY` | DECIMAL(11,2) |  |  |  |  |
| 13 | `NP_PRIMARY_UM_CODE` | VARCHAR(3) |  |  |  |  |
| 14 | `NP_SECONDARY_QTY` | DECIMAL(11,2) |  |  |  |  |
| 15 | `NP_SECONDARY_UM_CODE` | VARCHAR(3) |  |  |  |  |
| 16 | `NP_PACKAGING_QTY` | DECIMAL(9,2) |  |  |  |  |
| 17 | `NP_PACKAGING_UM_CODE` | VARCHAR(3) |  |  |  |  |
| 18 | `NP_PERCENT_IN_PROGRESS` | DECIMAL(12,9) |  |  |  |  |
| 19 | `NP_FINAL_TO_INITIAL_DIVIDER` | DECIMAL(12,9) |  |  |  |  |
| 20 | `NP_CLOSED_STEP` | CHAR(1) |  |  |  |  |
| 21 | `NP_BASE_PRIMARY_UM_CODE` | VARCHAR(3) |  |  |  |  |
| 22 | `NP_MULT_TO_BASE_PRIMARY_UMCODE` | DECIMAL(15,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.NP_IDENTIFIER,
       t.NP_PROGRESS_NUMBER,
       t.NP_PROGRESS_TAMPLATECODE,
       t.NP_DEMAND_COUNTER_CODE,
       t.NP_DEMAND_CODE,
       t.NP_DEMAND_STEP,
       t.NP_DEMAND_TEMPLATE_CODE,
       t.NP_PRODUCTION_ORDER_CODE,
       t.NP_ORIG_END_DATE,
       t.NP_START_DATE_TIME,
       t.NP_END_DATE_TIME,
       t.NP_RESOURCE_CODE
FROM   DB2ADMIN.SCDA_NOW_PROGRESS t
FETCH FIRST 100 ROWS ONLY;
```
