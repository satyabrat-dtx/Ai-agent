# DB2ADMIN.WRKNETEXTOPDETAILDOCUMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239645

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CUSER` | CHAR(50) |  |  |  |  |
| 4 | `EXTOPDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `EXTOPDOCUMENTPROVCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `EXTOPDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 7 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `EXTITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 10 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 11 | `EXTERNOPLINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `EXTERNOPLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 13 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 16 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 17 | `EXTERNOPLINECODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.CUSER,
       t.EXTOPDOCUMENTCOMPANYCODE,
       t.EXTOPDOCUMENTPROVCOUNTERCODE,
       t.EXTOPDOCUMENTPROVISIONALCODE,
       t.BASICVALUE,
       t.ITEMDESCRIPTION,
       t.EXTITEMDESCRIPTION,
       t.ITEMTYPEAFICODE,
       t.EXTERNOPLINECOUNTERCODE
FROM   DB2ADMIN.WRKNETEXTOPDETAILDOCUMENT t
FETCH FIRST 100 ROWS ONLY;
```
