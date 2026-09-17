# DB2ADMIN.WRKFINTRAILBALANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178736

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `GLCODE` | CHAR(20) |  |  |  |  |
| 6 | `OBDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `OBCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `FINMONTH` | INTEGER | NOT NULL |  |  |  |
| 9 | `TRDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `TRCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `FINDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 12 | `NETDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `NETCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `RECONCILATIONFLAG` | SMALLINT | NOT NULL |  |  |  |
| 15 | `GLDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 16 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 17 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 18 | `SLCUSTOMERSUPPLIERDESC` | VARCHAR(270) |  |  |  |  |
| 19 | `OBDRCHAR` | CHAR(25) |  |  |  |  |
| 20 | `OBCRCHAR` | CHAR(25) |  |  |  |  |
| 21 | `TRDRCHAR` | CHAR(25) |  |  |  |  |
| 22 | `TRCRCHAR` | CHAR(25) |  |  |  |  |
| 23 | `CLOSINGDR` | CHAR(25) |  |  |  |  |
| 24 | `CLOSINGCR` | CHAR(25) |  |  |  |  |
| 25 | `BUSINESSUNITDESC` | VARCHAR(200) |  |  |  |  |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINTRAILBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.FINANCIALYEARCODE,
       t.BUSINESSUNITCODE,
       t.GLCODE,
       t.OBDEBIT,
       t.OBCREDIT,
       t.FINMONTH,
       t.TRDEBIT,
       t.TRCREDIT,
       t.FINDOCUMENTCODE
FROM   DB2ADMIN.WRKFINTRAILBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
