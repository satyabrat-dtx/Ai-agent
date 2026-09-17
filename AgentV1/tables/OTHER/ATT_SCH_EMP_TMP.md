# DB2ADMIN.ATT_SCH_EMP_TMP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `no_primary_key`
- **Columns**: 37
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181829

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | VARCHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | VARCHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 2 | `CATEGORYICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 3 | `CATEGORYCODE` | VARCHAR(6) |  |  |  |  |
| 4 | `CATEGORYTYPE` | DECIMAL(10,0) |  |  |  |  |
| 5 | `CODE` | VARCHAR(9) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `FACTORYCODE` | VARCHAR(3) |  |  |  |  |
| 7 | `DEPARTMENTDEPARTMENTCODE` | VARCHAR(8) |  |  |  |  |
| 8 | `SECTIONSECTIONICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 9 | `SECTIONSECTIONCODE` | VARCHAR(6) |  |  |  |  |
| 10 | `MATYPEMACHINETYPEICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 11 | `MACHINETYPEMACHINETYPECODE` | VARCHAR(6) |  |  |  |  |
| 12 | `MACHINENOMACHINENOICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 13 | `MACHINENOMACHINENOCODE` | VARCHAR(6) |  |  |  |  |
| 14 | `GRADEICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 15 | `GRADECODE` | VARCHAR(6) |  |  |  |  |
| 16 | `CADREICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 17 | `CADRECODE` | VARCHAR(6) |  |  |  |  |
| 18 | `DESGDESIGNATIONICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 19 | `DESGDESIGNATIONCODE` | VARCHAR(6) |  |  |  |  |
| 20 | `EMPROLECODE` | VARCHAR(3) |  |  |  |  |
| 21 | `SUBCTGSUBCATEGORYICSTABLECODE` | VARCHAR(4) |  |  |  |  |
| 22 | `SUBCATEGORYSUBCATEGORYCODE` | VARCHAR(6) |  |  |  |  |
| 23 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 24 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 25 | `CONFIRMATIONDATE` | DATE |  |  |  |  |
| 26 | `RESIGNDATE` | DATE |  |  |  |  |
| 27 | `JOININGDATE` | DATE |  |  |  |  |
| 28 | `CREATIONTIMESTAMP` | BIGINT |  |  | audit |  |
| 29 | `SERIAL` | DECIMAL(10,0) |  |  |  |  |
| 30 | `COSTCENTERBADLICODE` | VARCHAR(10) |  |  |  |  |
| 31 | `HOLIDAYCODE` | VARCHAR(3) |  |  |  |  |
| 32 | `EFFECTIVEDATE` | DATE |  |  |  |  |
| 33 | `SHIFTROTATIONCODE` | VARCHAR(3) |  |  |  |  |
| 34 | `WEEKLYOFF` | DECIMAL(10,0) |  |  |  |  |
| 35 | `FREQUENCY` | DECIMAL(10,0) |  |  |  |  |
| 36 | `FREQUENCYDAYS` | DECIMAL(10,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CATEGORYICSTABLECODE,
       t.CATEGORYCODE,
       t.CATEGORYTYPE,
       t.CODE,
       t.FACTORYCODE,
       t.DEPARTMENTDEPARTMENTCODE,
       t.SECTIONSECTIONICSTABLECODE,
       t.SECTIONSECTIONCODE,
       t.MATYPEMACHINETYPEICSTABLECODE,
       t.MACHINETYPEMACHINETYPECODE
FROM   DB2ADMIN.ATT_SCH_EMP_TMP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
