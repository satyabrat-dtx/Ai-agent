# DB2ADMIN.WRKUSAPMWORKORDERSTATUSPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115573

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `MAINCATEGORY` | CHAR(3) |  |  |  |  |
| 6 | `PMWORKORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `PMWORKORDERCODE` | CHAR(15) |  |  |  |  |
| 8 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 10 | `PLANTDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 11 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 12 | `DEPARTMENTDESCRIPTIONS` | VARCHAR(100) |  |  |  |  |
| 13 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 15 | `PMBOMDESCRIPTIONS` | VARCHAR(100) |  |  |  |  |
| 16 | `PRVMAINTENANCECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 17 | `PREVENTIVEMAINTENANCECODE` | CHAR(15) |  |  |  |  |
| 18 | `PMPRVMNTDESCRIPTIONS` | VARCHAR(100) |  |  |  |  |
| 19 | `PMBREAKDOWNENTRYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 20 | `PMBREAKDOWNENTRYCODE` | CHAR(15) |  |  |  |  |
| 21 | `SYMPTOM` | VARCHAR(1000) | NOT NULL |  |  |  |
| 22 | `SCHEDULEDATE` | DATE |  |  |  |  |
| 23 | `PLANNEDSCHDDATE` | DATE |  |  |  |  |
| 24 | `ASSIGNEDBYUSERID` | CHAR(25) |  |  |  |  |
| 25 | `ASSIGNEDTOUSERID` | CHAR(25) |  |  |  |  |
| 26 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 27 | `CATEGORY` | INTEGER | NOT NULL |  |  |  |

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
       t.MAINCATEGORY,
       t.PMWORKORDERCOUNTERCODE,
       t.PMWORKORDERCODE,
       t.TEMPLATECODE,
       t.PLANTCODE,
       t.PLANTDESCRIPTION,
       t.DEPARTMENTCODE
FROM   DB2ADMIN.WRKUSAPMWORKORDERSTATUSPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
