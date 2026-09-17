# DB2ADMIN.SHIPPINGTIMEDEFINITION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `COMPANYCODE`, `TERMSOFDELIVERYCODE`, `TERMSOFSHIPPINGCODE`, `AREACODE`, `CARRIERTYPE`, `CARRIERCODE`, `INITIALDATE`, `FINALDATE`, `FROMTRANSPORTCOUNTRYCODE`, `FROMTRANSPORTCODE`, `TOTRANSPORTCOUNTRYCODE`, `TOTRANSPORTCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112328

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `TERMSOFDELIVERYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `TERMSOFSHIPPINGCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `TERMSOFSHIPPINGCODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `AREACOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `AREACODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `CARRIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 8 | `CARRIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 9 | `INITIALDATE` | DATE | NOT NULL | PK | primary_key |  |
| 10 | `FINALDATE` | DATE | NOT NULL | PK | primary_key |  |
| 11 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 12 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 13 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 14 | `SHIPPINGLEADTIME` | INTEGER | NOT NULL |  |  |  |
| 15 | `SHIPPINGCALENDARCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `TRANSPORTLEADTIME` | INTEGER | NOT NULL |  |  |  |
| 17 | `TRANSPORTCALENDARCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `FROMTRANSPORTCOUNTRYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 26 | `FROMTRANSPORTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 27 | `TOTRANSPORTCOUNTRYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 28 | `TOTRANSPORTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SHIPPINGTIMEDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `WORKINGCALENDAR_SHIPPINGCALENDAR` | `SHIPPINGCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `SHIPPINGTIMEDEFINITION.SHIPPINGCALENDARCODE = WORKINGCALENDAR.CODE` |
| `WORKINGCALENDAR_TRANSPORTCALENDAR` | `TRANSPORTCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `SHIPPINGTIMEDEFINITION.TRANSPORTCALENDARCODE = WORKINGCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SHIPPINGTIMEDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TERMSOFDELIVERYCOMPANYCODE,
       t.TERMSOFDELIVERYCODE,
       t.TERMSOFSHIPPINGCOMPANYCODE,
       t.TERMSOFSHIPPINGCODE,
       t.AREACOMPANYCODE,
       t.AREACODE,
       t.CARRIERTYPE,
       t.CARRIERCODE,
       t.INITIALDATE,
       t.FINALDATE,
       t.LONGDESCRIPTION
FROM   DB2ADMIN.SHIPPINGTIMEDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
