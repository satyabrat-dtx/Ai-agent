# DB2ADMIN.WRKPACKINGCREDIT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 37
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`, `COMPANYCODE`, `LETTERNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177857

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 5 | `LETTERNO` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 6 | `BANKCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `BANKCODE` | CHAR(20) |  |  |  |  |
| 8 | `PACKINGDATE` | DATE |  |  |  |  |
| 9 | `ADJFORTHISBILL` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ADJUSTEDAMOUNTINR` | DECIMAL(18,5) |  |  |  |  |
| 11 | `AGENCYCOMMISSIONRATE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `BALANCEAMOUNTINR` | DECIMAL(18,5) |  |  |  |  |
| 13 | `LOANREQUISITIONAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 14 | `UNUTILIZEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `LOANINTERESTRATE` | DECIMAL(6,3) | NOT NULL |  |  |  |
| 16 | `FOREGINCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 17 | `FCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 18 | `EXCHANGERATE` | DECIMAL(28,15) |  |  |  |  |
| 19 | `INTERESTCHARGED` | CHAR(1) |  |  |  |  |
| 20 | `SHIPMENTDETAILS` | CHAR(50) |  |  |  |  |
| 21 | `STATUS` | CHAR(10) |  |  |  |  |
| 22 | `BANKREFNO` | CHAR(30) |  |  |  |  |
| 23 | `BANKADVICEDATE` | DATE |  |  |  |  |
| 24 | `LOANSANCTIONEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 25 | `PCGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `PCGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 27 | `DUEDATE` | DATE |  |  |  |  |
| 28 | `BANKCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 29 | `BANKCHARGESGLACCOUNTCODE` | CHAR(20) |  |  |  |  |
| 30 | `ACTUALCHARGES` | DECIMAL(18,5) |  |  |  |  |
| 31 | `PROFITCENTERPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 32 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 33 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 34 | `ANALITICALCODE` | CHAR(15) |  |  |  |  |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `BCHARGESGLACCOUNTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPACKINGCREDITUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.CHOOSE,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.LETTERNO,
       t.BANKCOMPANYCODE,
       t.BANKCODE,
       t.PACKINGDATE,
       t.ADJFORTHISBILL,
       t.ADJUSTEDAMOUNTINR,
       t.AGENCYCOMMISSIONRATE
FROM   DB2ADMIN.WRKPACKINGCREDIT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
