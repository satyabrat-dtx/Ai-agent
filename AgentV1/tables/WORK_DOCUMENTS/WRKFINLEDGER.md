# DB2ADMIN.WRKFINLEDGER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178444

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `FINDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 5 | `POSTINGDATE` | DATE |  |  |  |  |
| 6 | `OBDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 7 | `OBCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `TRDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TRCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `CLOSINGDEBIT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `CLOSINGCREDIT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `GLCODE` | CHAR(20) |  |  |  |  |
| 13 | `OPENINGBALANCEAMT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `GLDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 16 | `BUSINESSUNITDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 17 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 18 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 20 | `SLCUSTOMERSUPPLIERDESC` | CHAR(8) |  |  |  |  |
| 21 | `OBDRCHAR` | CHAR(25) |  |  |  |  |
| 22 | `OBCRCHAR` | CHAR(25) |  |  |  |  |
| 23 | `TRDRCHAR` | CHAR(25) |  |  |  |  |
| 24 | `TRCRCHAR` | CHAR(25) |  |  |  |  |
| 25 | `CLOSINGDR` | CHAR(25) |  |  |  |  |
| 26 | `CLOSINGCR` | CHAR(25) |  |  |  |  |
| 27 | `COMMENTS` | VARCHAR(255) |  |  |  |  |
| 28 | `CHEQUENUMBER` | CHAR(20) |  |  |  |  |
| 29 | `REFERENCETEXT1` | CHAR(20) |  |  |  |  |
| 30 | `REFERENCETEXT2` | CHAR(20) |  |  |  |  |
| 31 | `REFERENCETEXT3` | CHAR(20) |  |  |  |  |
| 32 | `TDSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINLEDGERUID` (ABSUNIQUEID)
- `GLINDEX` (CREATIONTIMESTAMP, COMPANYCODE, BUSINESSUNITCODE, GLCODE, SLCUSTOMERSUPPLIERTYPE, SLCUSTOMERSUPPLIERCODE)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.TEMPLATECODE,
       t.FINDOCUMENTCODE,
       t.POSTINGDATE,
       t.OBDEBIT,
       t.OBCREDIT,
       t.TRDEBIT,
       t.TRCREDIT,
       t.CLOSINGDEBIT,
       t.CLOSINGCREDIT
FROM   DB2ADMIN.WRKFINLEDGER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
