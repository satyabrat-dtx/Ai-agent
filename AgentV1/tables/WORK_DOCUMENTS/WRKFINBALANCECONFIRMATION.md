# DB2ADMIN.WRKFINBALANCECONFIRMATION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224191

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 6 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 8 | `ORDERPARTNERNAME` | VARCHAR(200) |  |  |  |  |
| 9 | `ASONDATE` | DATE | NOT NULL |  |  |  |
| 10 | `SUMOFAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CONFIRMEDTOBEWITHDATE` | DATE |  |  |  |  |
| 12 | `AMOUNTTYPE` | CHAR(2) |  |  |  |  |
| 13 | `INVOICEBREAKUPREQUIRED` | CHAR(1) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINBALANCECONFIRMATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.ORDERPARTNERNAME,
       t.ASONDATE,
       t.SUMOFAMOUNTINCC,
       t.CONFIRMEDTOBEWITHDATE
FROM   DB2ADMIN.WRKFINBALANCECONFIRMATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
