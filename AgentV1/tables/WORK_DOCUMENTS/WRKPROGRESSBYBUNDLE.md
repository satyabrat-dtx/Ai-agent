# DB2ADMIN.WRKPROGRESSBYBUNDLE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 106770

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 6 | `ELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `ELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 9 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 10 | `PRIMARYQUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 11 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.DEMANDCOUNTERCODE,
       t.DEMANDCODE,
       t.ELEMENTCOMPANYCODE,
       t.ELEMENTITEMTYPECODE,
       t.ELEMENTSUBCODEKEY,
       t.ELEMENTCODE,
       t.PRIMARYQUANTITY,
       t.PRIMARYUOMCODE
FROM   DB2ADMIN.WRKPROGRESSBYBUNDLE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
