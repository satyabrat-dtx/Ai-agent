# DB2ADMIN.WRKPMSERVICEREQRPT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 84907

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 3 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 4 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 5 | `BREAKDOWNCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 6 | `BREAKDOWNCODE` | CHAR(15) |  |  |  |  |
| 7 | `PRVMAINTENANCECOUNTERCODE` | CHAR(15) |  |  |  |  |
| 8 | `PREVENTIVEMAINTENANCECODE` | CHAR(15) |  |  |  |  |
| 9 | `PMMACHINECOUNTERCODE` | CHAR(15) |  |  |  |  |
| 10 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 11 | `LINENO` | DECIMAL(10,0) | NOT NULL | PK | primary_key |  |
| 12 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 13 | `ESTIMATEDDURATION` | DECIMAL(11,2) |  |  |  |  |
| 14 | `DURATIONUOMCODE` | INTEGER | NOT NULL |  |  |  |
| 15 | `RESOURCESCODE` | CHAR(6) |  |  |  |  |
| 16 | `NEXTSCHEDULE` | INTEGER | NOT NULL |  |  |  |
| 17 | `WORKINGCALENDARCODE` | CHAR(3) |  |  |  |  |
| 18 | `SCHEDULEDDATE` | DATE |  |  |  |  |
| 19 | `SCHEDULEID` | INTEGER | NOT NULL |  |  |  |
| 20 | `IDENTIFIEDDATE` | TIMESTAMP |  |  |  |  |
| 21 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 22 | `SYMPTOM` | VARCHAR(1000) |  |  |  |  |
| 23 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 24 | `WORKORDERCREATED` | INTEGER | NOT NULL |  |  |  |
| 25 | `REMARKS` | VARCHAR(1000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.PLANTCODE,
       t.DIVISIONCODE,
       t.DEPARTMENTCODE,
       t.BREAKDOWNCOUNTERCODE,
       t.BREAKDOWNCODE,
       t.PRVMAINTENANCECOUNTERCODE,
       t.PREVENTIVEMAINTENANCECODE,
       t.PMMACHINECOUNTERCODE,
       t.PMMACHINECODE,
       t.LINENO
FROM   DB2ADMIN.WRKPMSERVICEREQRPT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
