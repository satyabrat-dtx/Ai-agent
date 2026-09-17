# DB2ADMIN.WRKFINCHEQUEPRINTING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `CREATIONTIMESTAMP`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178141

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CHEQUEDATE` | DATE |  |  |  |  |
| 4 | `BENEFICIARYNAME` | VARCHAR(200) |  |  |  |  |
| 5 | `CHEQUEAMT` | DECIMAL(18,5) |  |  |  |  |
| 6 | `DOCUMENTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 7 | `DOCCOMPANYCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINCHEQUEPRINTINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENUMBER,
       t.COMPANYCODE,
       t.CHEQUEDATE,
       t.BENEFICIARYNAME,
       t.CHEQUEAMT,
       t.DOCUMENTCURRENCYCODE,
       t.DOCCOMPANYCURRENCYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKFINCHEQUEPRINTING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
