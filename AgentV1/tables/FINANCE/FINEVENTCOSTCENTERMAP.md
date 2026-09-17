# DB2ADMIN.FINEVENTCOSTCENTERMAP

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `EVENTCODE`, `DIVISIONCODE`, `MRNPREFIXCODE`, `INVOICETYPECODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175232

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EVENTCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 4 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 7 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 8 | `COSTCENTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `COSTCENTERCODE` | CHAR(20) |  | FK | foreign_key |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINEVENTCOSTCENTERMAP.COMPANYCODE = COMPANY.CODE` |
| `COSTCENTER_COSTCENTER` | `COSTCENTERCOMPANYCODE`, `COSTCENTERCODE` | [`COSTCENTER`](../COSTING/COSTCENTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEVENTCOSTCENTERMAP.COSTCENTERCOMPANYCODE = COSTCENTER.COMPANYCODE AND FINEVENTCOSTCENTERMAP.COSTCENTERCODE = COSTCENTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEVENTCOSTCENTERMAP.COMPANYCODE = DIVISION.COMPANYCODE AND FINEVENTCOSTCENTERMAP.DIVISIONCODE = DIVISION.CODE` |
| `EVENTMASTER_EVENT` | `EVENTCODE` | [`EVENTMASTER`](../CORE_MASTER/EVENTMASTER.md) | `CODE` | RESTRICT | `FINEVENTCOSTCENTERMAP.EVENTCODE = EVENTMASTER.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEVENTCOSTCENTERMAP.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINEVENTCOSTCENTERMAP.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEVENTCOSTCENTERMAPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.EVENTCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.INVOICETYPECODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.COSTCENTERCOMPANYCODE,
       t.COSTCENTERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINEVENTCOSTCENTERMAP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
