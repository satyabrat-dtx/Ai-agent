# DB2ADMIN.WRKFINOUTSTANDINGBALANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178524

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `ACTUALCREATIONTIMESTAMP` | BIGINT | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 6 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 7 | `GLCODE` | CHAR(20) |  |  |  |  |
| 8 | `FINDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 9 | `NETDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `NETCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `GLDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 12 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 13 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 15 | `SLCUSTOMERSUPPLIERDESC` | CHAR(100) |  |  |  |  |
| 16 | `DOCUMENTTEMPLATE` | CHAR(3) |  |  |  |  |
| 17 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 18 | `DUEDATE` | DATE |  |  |  |  |
| 19 | `AMOUNTINDC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 20 | `DOCUMENTCURRENCY` | CHAR(4) |  |  |  |  |
| 21 | `AMOUNTINCC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 22 | `COMPANYCURRENCY` | CHAR(4) |  |  |  |  |
| 23 | `SLAB1` | DECIMAL(18,5) |  |  |  |  |
| 24 | `SLAB2` | DECIMAL(18,5) |  |  |  |  |
| 25 | `SLAB3` | DECIMAL(18,5) |  |  |  |  |
| 26 | `SLAB4` | DECIMAL(18,5) |  |  |  |  |
| 27 | `SLAB5` | DECIMAL(18,5) |  |  |  |  |
| 28 | `CLEAREDAMOUNT` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.ACTUALCREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.GLCODE,
       t.FINDOCUMENTCODE,
       t.NETDEBIT,
       t.NETCREDIT,
       t.GLDESCRIPTION
FROM   DB2ADMIN.WRKFINOUTSTANDINGBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
