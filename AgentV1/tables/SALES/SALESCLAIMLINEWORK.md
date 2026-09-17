# DB2ADMIN.SALESCLAIMLINEWORK

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 35235

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `SALDOCLINESALDOCPRVCNTCODE` | CHAR(8) |  |  |  |  |
| 5 | `SALDOCLINESALDOCPRVCODE` | CHAR(15) |  |  |  |  |
| 6 | `SALESDOCUMENTLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `SALESDOCUMENTLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `SALDOCLINECOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 10 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESCLAIMLINEWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.SALDOCLINESALDOCPRVCNTCODE,
       t.SALDOCLINESALDOCPRVCODE,
       t.SALESDOCUMENTLINEORDERLINE,
       t.SALESDOCUMENTLINEORDERSUBLINE,
       t.SALDOCLINECOMPONENTORDERLINE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SALESCLAIMLINEWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
