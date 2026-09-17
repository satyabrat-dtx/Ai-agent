# DB2ADMIN.WRKCONSOLIDATIONTB

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`, `FINANCIALYEARCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178074

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 5 | `GLCODE` | CHAR(20) |  |  |  |  |
| 6 | `OBDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `OBCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `TRDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TRCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `FINDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 11 | `NETDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `NETCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `RECONCILATIONFLAG` | SMALLINT | NOT NULL |  |  |  |
| 14 | `GLDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 16 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 17 | `SLCUSTOMERSUPPLIERDESC` | CHAR(100) |  |  |  |  |
| 18 | `OBDRCHAR` | CHAR(25) |  |  |  |  |
| 19 | `OBCRCHAR` | CHAR(25) |  |  |  |  |
| 20 | `TRDRCHAR` | CHAR(25) |  |  |  |  |
| 21 | `TRCRCHAR` | CHAR(25) |  |  |  |  |
| 22 | `CLOSINGDR` | CHAR(25) |  |  |  |  |
| 23 | `CLOSINGCR` | CHAR(25) |  |  |  |  |
| 24 | `DOCTYPEDESC` | VARCHAR(200) |  |  |  |  |
| 25 | `DOCTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `DOCTEMPDESC` | VARCHAR(200) |  |  |  |  |
| 27 | `DOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 28 | `COMPANYDESC` | VARCHAR(200) |  |  |  |  |
| 29 | `BUSINESSUNITDESC` | VARCHAR(200) |  |  |  |  |
| 30 | `CONSOLIDATIONCURRENCY` | CHAR(4) |  |  |  |  |
| 31 | `COMPANYCURRENCY` | CHAR(4) |  |  |  |  |
| 32 | `NETCREDITCOMPANYWISE` | DECIMAL(18,5) |  |  |  |  |
| 33 | `NETDEBITCOMPANYWISE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKCONSOLIDATIONTBUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCODE,
       t.GLCODE,
       t.OBDEBIT,
       t.OBCREDIT,
       t.TRDEBIT,
       t.TRCREDIT,
       t.FINDOCUMENTCODE,
       t.NETDEBIT
FROM   DB2ADMIN.WRKCONSOLIDATIONTB t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
