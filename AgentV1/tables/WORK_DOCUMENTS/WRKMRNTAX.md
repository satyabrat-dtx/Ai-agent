# DB2ADMIN.WRKMRNTAX

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239958

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `TAXCODETYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `CALCULATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `CALCULATEDVALUER` | DECIMAL(18,5) |  |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 10 | `TAXSEQUENCENO` | DECIMAL(2,0) |  |  |  |  |
| 11 | `TAXMRNNO` | DECIMAL(11,0) |  |  |  |  |
| 12 | `TAXABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |

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
       t.DIVISIONCODE,
       t.TAXCODETYPE,
       t.CALCULATIONTYPE,
       t.CALCULATEDVALUER,
       t.VALUE,
       t.SEARCHDESCRIPTION,
       t.TAXSEQUENCENO,
       t.TAXMRNNO
FROM   DB2ADMIN.WRKMRNTAX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
