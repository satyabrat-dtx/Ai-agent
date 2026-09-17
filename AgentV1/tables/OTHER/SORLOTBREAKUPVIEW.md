# DB2ADMIN.SORLOTBREAKUPVIEW

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `SODSALORDLINESALORDCOUNTERCOD`, `SODSALORDERLINESALESORDERCODE`, `SODSALESORDERLINEORDERLINE`, `SODSALESORDERLINEORDERSUBLINE`, `SODSALORDLINECOMPONENTORDLINE`, `SODDELIVERYLINE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205247

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `OPTIMUM` | CHAR(2) |  |  |  |  |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `INSERTTYPE` | CHAR(2) |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `SODSALORDLINESALORDCOUNTERCOD` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SODSALORDERLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SODSALESORDERLINEORDERLINE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `SODSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `SODSALORDLINECOMPONENTORDLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `SODDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 10 | `CONCATDELIVERYCODE` | VARCHAR(120) |  |  |  |  |
| 11 | `POSSIBLECASE` | INTEGER | NOT NULL |  |  |  |
| 12 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 13 | `PDCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 14 | `PDCODE` | CHAR(15) |  | FK | foreign_key |  |
| 15 | `BALLSPERCREEL` | DECIMAL(2,0) | NOT NULL |  |  |  |
| 16 | `WARPLOTLENGTH` | DECIMAL(15,2) |  |  |  |  |
| 17 | `ALLOWEDEXCESS` | DECIMAL(15,2) |  |  |  |  |
| 18 | `ALLWDEXCESS` | DECIMAL(15,2) |  |  |  |  |
| 19 | `ALLWDSHORTAGE` | DECIMAL(15,2) |  |  |  |  |
| 20 | `SOTOBEPLANNED` | DECIMAL(15,2) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `STMAX` | CHAR(2) |  |  |  |  |
| 28 | `STMIN` | CHAR(2) |  |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PRODUCTIONDEMAND_PD` | `COMPANYCODE`, `PDCOUNTERCODE`, `PDCODE` | [`PRODUCTIONDEMAND`](../PRODUCTION/PRODUCTIONDEMAND.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `SORLOTBREAKUPVIEW.COMPANYCODE = PRODUCTIONDEMAND.COMPANYCODE AND SORLOTBREAKUPVIEW.PDCOUNTERCODE = PRODUCTIONDEMAND.COUNTERCODE AND SORLOTBREAKUPVIEW.PDCODE = PRODUCTIONDEMAND.CODE` |
| `SALESORDERDELIVERY_SOD` | `COMPANYCODE`, `SODSALORDLINESALORDCOUNTERCOD`, `SODSALORDERLINESALESORDERCODE`, `SODSALESORDERLINEORDERLINE`, `SODSALESORDERLINEORDERSUBLINE`, `SODSALORDLINECOMPONENTORDLINE`, `SODDELIVERYLINE` | [`SALESORDERDELIVERY`](../SALES/SALESORDERDELIVERY.md) | `SALORDLINESALORDERCOMPANYCODE`, `SALORDLINESALORDERCOUNTERCODE`, `SALESORDERLINESALESORDERCODE`, `SALESORDERLINEORDERLINE`, `SALESORDERLINEORDERSUBLINE`, `SALORDLINECOMPONENTORDERLINE`, `DELIVERYLINE` | RESTRICT | `SORLOTBREAKUPVIEW.COMPANYCODE = SALESORDERDELIVERY.SALORDLINESALORDERCOMPANYCODE AND SORLOTBREAKUPVIEW.SODSALORDLINESALORDCOUNTERCOD = SALESORDERDELIVERY.SALORDLINESALORDERCOUNTERCODE AND SORLOTBREAKUPVIEW.SODSALORDERLINESALESORDERCODE = SALESORDERDELIVERY.SALESORDERLINESALESORDERCODE AND SORLOTBREAKUPVIEW.SODSALESORDERLINEORDERLINE = SALESORDERDELIVERY.SALESORDERLINEORDERLINE AND SORLOTBREAKUPVIEW.SODSALESORDERLINEORDERSUBLINE = SALESORDERDELIVERY.SALESORDERLINEORDERSUBLINE AND SORLOTBREAKUPVIEW.SODSALORDLINECOMPONENTORDLINE = SALESORDERDELIVERY.SALORDLINECOMPONENTORDERLINE AND SORLOTBREAKUPVIEW.SODDELIVERYLINE = SALESORDERDELIVERY.DELIVERYLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SORLOTBREAKUPVIEWUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.OPTIMUM,
       t.CHOOSE,
       t.INSERTTYPE,
       t.COMPANYCODE,
       t.SODSALORDLINESALORDCOUNTERCOD,
       t.SODSALORDERLINESALESORDERCODE,
       t.SODSALESORDERLINEORDERLINE,
       t.SODSALESORDERLINEORDERSUBLINE,
       t.SODSALORDLINECOMPONENTORDLINE,
       t.SODDELIVERYLINE,
       t.CONCATDELIVERYCODE,
       t.POSSIBLECASE
FROM   DB2ADMIN.SORLOTBREAKUPVIEW t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
