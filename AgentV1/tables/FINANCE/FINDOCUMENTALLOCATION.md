# DB2ADMIN.FINDOCUMENTALLOCATION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 46
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `FINMONTHFINANCIALYEARCODE`, `FINMONTHBUSINESSUNITCODE`, `FINMONTHCODE`, `GLCODE`, `LINE`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 179716

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 2 | `FINMONTHFINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 3 | `FINMONTHBUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `FINMONTHCODE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `GLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `GLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 10 | `PROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 11 | `FIRSTCODE` | CHAR(10) |  |  |  |  |
| 12 | `SECCODE` | CHAR(10) |  |  |  |  |
| 13 | `THIRDCODE` | CHAR(10) |  |  |  |  |
| 14 | `FOURTHCODE` | CHAR(10) |  |  |  |  |
| 15 | `FIFTHCODE` | CHAR(10) |  |  |  |  |
| 16 | `SIXTHCODE` | CHAR(10) |  |  |  |  |
| 17 | `SEVENTHCODE` | CHAR(10) |  |  |  |  |
| 18 | `DOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `DETAILBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 20 | `DETAILGLCODE` | CHAR(20) |  |  |  |  |
| 21 | `DETAILPROFITCENTERCODE` | CHAR(10) |  |  |  |  |
| 22 | `DETAILCOSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 23 | `DETAILFIRSTCODE` | CHAR(10) |  |  |  |  |
| 24 | `DETAILSECCODE` | CHAR(10) |  |  |  |  |
| 25 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 26 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 27 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 28 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 29 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 30 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 31 | `DETAILTHIRDCODE` | CHAR(10) |  |  |  |  |
| 32 | `DETAILFOURTHCODE` | CHAR(10) |  |  |  |  |
| 33 | `DETAILFIFTHCODE` | CHAR(10) |  |  |  |  |
| 34 | `DETAILSIXTHCODE` | CHAR(10) |  |  |  |  |
| 35 | `DETAILSEVENTHCODE` | CHAR(10) |  |  |  |  |
| 36 | `DETAILDOCUMENTAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 37 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 38 | `POSTFLAG` | SMALLINT | NOT NULL |  |  |  |
| 39 | `ALLOCATIONNUMBER` | CHAR(15) |  |  |  |  |
| 40 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 41 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 42 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 43 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 44 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 45 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINDOCUMENTALLOCATION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINDOCUMENTALLOCATIONUID` (ABSUNIQUEID)
- `IDXALLOCATIONNR` (COMPANYCODE, ALLOCATIONNUMBER)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINMONTHFINANCIALYEARCODE,
       t.FINMONTHBUSINESSUNITCODE,
       t.FINMONTHCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.SUBLINE,
       t.LINE,
       t.COSTCENTERCODE,
       t.PROFITCENTERCODE,
       t.FIRSTCODE
FROM   DB2ADMIN.FINDOCUMENTALLOCATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
