# DB2ADMIN.WRKFORWARDCONTRACT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177795

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `FCNO` | CHAR(10) |  |  |  |  |
| 6 | `FCLETTERDATE` | DATE |  |  |  |  |
| 7 | `STATUS` | CHAR(1) |  |  |  |  |
| 8 | `BANKCODECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 9 | `BANKCODECODE` | CHAR(20) |  |  |  |  |
| 10 | `PCGLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `PCGLCODE` | CHAR(20) |  |  |  |  |
| 12 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `FCRATE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `FCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `AGENCYCOMMISSIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ADJBILLAMT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 18 | `UTILISED` | DECIMAL(18,5) |  |  |  |  |
| 19 | `UNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 20 | `CANCELLEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `PURPOSE` | CHAR(3) |  |  |  |  |
| 22 | `DUEDATEFROM` | DATE |  |  |  |  |
| 23 | `REMARKS` | CHAR(50) |  |  |  |  |
| 24 | `BANKREFERENCENO` | CHAR(30) |  |  |  |  |
| 25 | `ADVICEDATE` | DATE |  |  |  |  |
| 26 | `BANKCHARGESGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 27 | `BANKCHARGESACTUAL` | DECIMAL(18,5) |  |  |  |  |
| 28 | `NARRATION` | CHAR(50) |  |  |  |  |
| 29 | `TENOR` | CHAR(1) |  |  |  |  |
| 30 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 31 | `BCHARGESGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFORWARDCONTRACTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.CHOOSE,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FCNO,
       t.FCLETTERDATE,
       t.STATUS,
       t.BANKCODECOMPANYCODE,
       t.BANKCODECODE,
       t.PCGLCOMPANYCODE,
       t.PCGLCODE
FROM   DB2ADMIN.WRKFORWARDCONTRACT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
