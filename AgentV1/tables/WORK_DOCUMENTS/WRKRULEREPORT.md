# DB2ADMIN.WRKRULEREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 877

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `RECORDTYPE` | CHAR(2) |  |  |  |  |
| 5 | `ORIGIN` | CHAR(2) |  |  |  |  |
| 6 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 8 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 9 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 11 | `TYPE` | CHAR(2) |  |  |  |  |
| 12 | `RULECODE` | CHAR(10) |  |  |  |  |
| 13 | `PRERULEFOUND` | SMALLINT | NOT NULL |  |  |  |
| 14 | `BOMCMPBILLOFMATERIALNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 15 | `BOMCOMPONENTSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 16 | `BOMCOMPONENTSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `BOMITEMCODE` | VARCHAR(120) |  |  |  |  |
| 18 | `BOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 19 | `ROUTINGSTEPROUTINGNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 20 | `ROUTINGSTEPSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 21 | `ROUTINGSTEPSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 22 | `RTGITEMCODE` | VARCHAR(120) |  |  |  |  |
| 23 | `RTGSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 24 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 25 | `MESSAGETXT` | VARCHAR(250) |  |  |  |  |
| 26 | `COLOR` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.RECORDTYPE,
       t.ORIGIN,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.ITEMCODE,
       t.QUANTITY,
       t.UOMCODE,
       t.TYPE
FROM   DB2ADMIN.WRKRULEREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
