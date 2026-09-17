# DB2ADMIN.WRKWORKORDERREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108997

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 9 | `PLANTDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 11 | `DEPARTMENTDESCRIPTIONS` | VARCHAR(200) |  |  |  |  |
| 12 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 13 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 14 | `PMBOMDESCRIPTIONS` | VARCHAR(200) |  |  |  |  |
| 15 | `PRVMAINTENANCECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 16 | `PREVENTIVEMAINTENANCECODE` | CHAR(15) |  |  |  |  |
| 17 | `PMPRVMNTDESCRIPTIONS` | VARCHAR(200) |  |  |  |  |
| 18 | `PMBREAKDOWNENTRYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 19 | `PMBREAKDOWNENTRYCODE` | CHAR(15) |  |  |  |  |
| 20 | `SYMPTOM` | VARCHAR(1000) | NOT NULL |  |  |  |
| 21 | `SCHEDULEDATE` | DATE |  |  |  |  |
| 22 | `PLANNEDSCHDDATE` | DATE |  |  |  |  |
| 23 | `ASSIGNEDBYUSERID` | CHAR(50) |  |  |  |  |
| 24 | `ASSIGNEDTOUSERID` | CHAR(50) |  |  |  |  |
| 25 | `REMARKS` | VARCHAR(1000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.STATUS,
       t.PMWORKORDERCOUNTERCODE,
       t.PMWORKORDERCODE,
       t.TEMPLATECODE,
       t.PLANTCODE,
       t.PLANTDESCRIPTION,
       t.DEPARTMENTCODE,
       t.DEPARTMENTDESCRIPTIONS
FROM   DB2ADMIN.WRKWORKORDERREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
