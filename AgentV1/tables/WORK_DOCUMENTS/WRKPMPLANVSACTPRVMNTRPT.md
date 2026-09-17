# DB2ADMIN.WRKPMPLANVSACTPRVMNTRPT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84867

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SCHEDULEID` | INTEGER | NOT NULL |  |  |  |
| 4 | `PLANNEDDATE` | DATE |  |  |  |  |
| 5 | `PRVMNTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PRVMNTCODE` | CHAR(15) |  |  |  |  |
| 7 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 8 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 9 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 10 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 12 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 14 | `ACTUALDATE` | DATE |  |  |  |  |
| 15 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 16 | `EXECUTIONSTARTDATE` | TIMESTAMP |  |  |  |  |
| 17 | `EXECUTIONENDDATE` | TIMESTAMP |  |  |  |  |
| 18 | `WORKORDERCREATED` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.SCHEDULEID,
       t.PLANNEDDATE,
       t.PRVMNTCOUNTERCODE,
       t.PRVMNTCODE,
       t.PLANTCODE,
       t.DIVISIONCODE,
       t.DEPARTMENTCODE,
       t.WORKCENTERCODE,
       t.COSTCENTERCODE
FROM   DB2ADMIN.WRKPMPLANVSACTPRVMNTRPT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
